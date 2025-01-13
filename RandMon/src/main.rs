use crossterm::{
    execute,
    style::Print,
    terminal::{Clear, ClearType},
    cursor::MoveTo,
    event::{self, Event, KeyCode},
    ExecutableCommand,
};
use clap::Parser;
use rand::Rng;
use std::{
    error::Error,
    io::{stdout, Write},
    thread,
    time::{Duration, Instant},
};

/// A simple Matrix-style random character display tool.
#[derive(Parser)]
struct Args {
    /// Refresh rate in Hertz (default: 30 Hz)
    #[arg(short, long, default_value = "30")]
    frequency: u64,
}

fn main() -> Result<(), Box<dyn Error>> {
    // Parse command-line arguments
    let args = Args::parse();

    // Calculate delay per frame based on frequency
    let delay = Duration::from_secs_f64(1.0 / args.frequency as f64);

    // Prepare terminal
    let mut stdout = stdout();
    stdout.execute(Clear(ClearType::All))?;

    // Character set for random display
    let charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        .chars()
        .collect::<Vec<_>>();
    let mut rng = rand::thread_rng();

    let mut paused = false;

    loop {
        let start_time = Instant::now();

        // Check for keyboard input
        if event::poll(Duration::from_millis(1))? {
            if let Event::Key(key_event) = event::read()? {
                match key_event.code {
                    KeyCode::Char(' ') => paused = !paused, // Toggle pause on Spacebar
                    KeyCode::Char('q') => break,           // Exit on 'q'
                    _ => {}
                }
            }
        }

        if !paused {
            for _ in 0..1000 {
                let x = rng.gen_range(0..48); // Adjust columns
                let y = rng.gen_range(0..64); // Adjust rows
                let char = charset[rng.gen_range(0..charset.len())];
                execute!(
                    stdout,
                    MoveTo(x, y),
                    Print(char)
                )?;
            }
            stdout.flush()?;
        }

        // Maintain the refresh rate
        let elapsed = start_time.elapsed();
        if elapsed < delay {
            thread::sleep(delay - elapsed);
        }
    }

    Ok(())
}
