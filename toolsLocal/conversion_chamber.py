from math import log, ceil

class RadixError(ValueError):
    pass

def _validate_alphabet(alpha: str):
    if not alpha:
        raise RadixError("Alphabet darf nicht leer sein.")
    if len(set(alpha)) != len(alpha):
        raise RadixError("Alphabet enthält Duplikate.")
    return alpha

def _strip_sign(s: str):
    if s.startswith('-'):
        return -1, s[1:]
    return 1, s

def decode_to_int(s: str, alphabet: str, max_input_len: int = 1_000_000) -> int:
    """Dekodiert s aus Alphabet -> Python-Integer. Unterstützt unär (Basis 1)."""
    alphabet = _validate_alphabet(alphabet)
    sign, core = _strip_sign(s.strip())
    if len(core) > max_input_len:
        raise RadixError("Input zu lang für Policy.")
    if core == "":
        return 0
    base = len(alphabet)

    if base == 1:
        # Unär: Wert = Anzahl Symbole; jeder Char muss das einzige Symbol sein
        sym = alphabet[0]
        if any(c != sym for c in core):
            raise RadixError("Ungültiges Zeichen im unären System.")
        return sign * len(core)

    # Map für Ziffernwerte
    val = {ch: i for i, ch in enumerate(alphabet)}
    try:
        n = 0
        for ch in core:
            d = val[ch]  # KeyError → ungültiges Zeichen
            n = n * base + d
    except KeyError:
        raise RadixError(f"Ungültiges Zeichen: {ch!r}")
    return sign * n

def encode_from_int(n: int, alphabet: str, pad: int = 0, max_output_len: int = 1_000_000) -> str:
    """Kodiert Integer n in Zielalphabet. Unterstützt unär (Basis 1)."""
    alphabet = _validate_alphabet(alphabet)
    base = len(alphabet)

    if n == 0:
        out = alphabet[0] if base > 1 else ""
        # pad auf Länge auffüllen (nur sinnvoll für base>1)
        if base > 1 and pad > 1:
            out = out.rjust(pad, alphabet[0])
        return out

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    if base == 1:
        # Unär: n-mal das Symbol
        if n > max_output_len:
            raise RadixError("Unäre Ausgabe überschreitet Limit.")
        return sign + (alphabet[0] * n)

    digits = []
    while n:
        n, r = divmod(n, base)
        digits.append(alphabet[r])
        if len(digits) > max_output_len:
            raise RadixError("Ausgabe überschreitet Limit.")
    out = "".join(reversed(digits))
    if pad > 0 and len(out) < pad:
        out = out.rjust(pad, alphabet[0])
    return sign + out

def estimate_output_len(n_or_str, src_alpha: str, dst_alpha: str) -> int:
    """Grobe Obergrenze der Ziffern in Zielbasis (für Limits/Preflight).
       Akzeptiert Integer oder Eingabestring (dann wird erst dekodiert)."""
    if not isinstance(n_or_str, int):
        N = decode_to_int(n_or_str, src_alpha)
    else:
        N = n_or_str
    if N == 0:
        return 1 if len(dst_alpha) > 1 else 0
    if len(dst_alpha) == 1:
        return N  # unär: Länge = Zahl
    # ceil(log_b(N+1))
    return ceil(log(N + 1, len(dst_alpha)))

def convert(value: str, src_alpha: str, dst_alpha: str,
            max_in: int = 1_000_000, max_out: int = 1_000_000, pad: int = 0) -> str:
    """General-purpose Konverter von (value, src_alpha) -> dst_alpha."""
    N = decode_to_int(value, src_alpha, max_input_len=max_in)
    # Preflight: Abschätzung Ziel-Länge
    est = estimate_output_len(N, src_alpha, dst_alpha)
    if est > max_out:
        raise RadixError(f"Zielausgabe ({est} Zeichen) überschreitet Limit ({max_out}).")
    return encode_from_int(N, dst_alpha, pad=pad, max_output_len=max_out)

