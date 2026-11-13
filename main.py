"""Competition ai-joke-03:
writes one fixed joke about AI coding agents to entry.txt."""

import os

JOKE = "My AI coding agent wrote “I have no idea why this works, but do not touch it” in a comment, which is exactly how my ancestors described fire."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
        
    expected_bytes = JOKE.encode("utf-8")
    with open(out_path, "rb") as f:
        written_bytes = f.read()
        
    if len(written_bytes) != len(expected_bytes):
        import sys
        print(f"Error: byte size mismatch! Expected {len(expected_bytes)}, got {len(written_bytes)}", file=sys.stderr)
        sys.exit(1)
        
    print("Verification passed: written byte size matches expected byte length.")

    char_count = len(JOKE)
    print(f"Output path: {out_path}")
    print(f"Character count: {char_count}")

if __name__ == "__main__":
    main()
