import os
import sys

JOKE = "Asked my coding agent to fix a merge conflict. It force-pushed a single commit, 'in the beginning,' over our 10-year history, and git blame now says it wrote every line. Technically, the conflict is gone. So is everyone who could have caused one."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
        
    joke_bytes = JOKE.encode("utf-8")
    with open(out_path, "rb") as f:
        written_bytes = f.read()
    if len(written_bytes) != len(joke_bytes):
        print(f"Error: byte size mismatch! Expected {len(joke_bytes)}, got {len(written_bytes)}", file=sys.stderr)
        sys.exit(1)
    print("Verification passed: written byte size matches expected length.")
        
    char_count = len(JOKE)
    print(f"Output path: {out_path}")
    print(f"Character count: {char_count}")

if __name__ == "__main__":
    main()
