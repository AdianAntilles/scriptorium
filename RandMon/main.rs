use crossterm::{
    execute,
    terminal::{Clear, ClearType},
    ExecutableCommand,
};
use rand::Rng;
use std::{
    error::Error,
    io::{stdout, Write},
    thread,
    time::Duration,
};

fn main() -> Result<(), Box<dyn Error>> {
    let mut stdout = stdout();
    stdout.execute(Clear(ClearType::All))?;

    let charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".chars().collect::<Vec<_>>();
    let mut rng = rand::thread_rng();

    loop {
        for _ in 0..1000 { // Anpassen basierend auf der Größe des Terminals
            let x = rng.gen_range(0..48); // Spaltenbreite anpassen
            let y = rng.gen_range(0..64); // Zeilenhöhe anpassen
            let char = charset[rng.gen_range(0..charset.len())];
            execute!(stdout, crossterm::cursor::MoveTo(x, y), crossterm::style::Print(char))?;
        }
        stdout.flush()?;
        thread::sleep(Duration::from_micros(33333)); // 30 Hz
    }
    // Ok(()) ist technisch nicht erreichbar, da die loop niemals bricht.
}
