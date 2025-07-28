#!/usr/bin/env python3
import os
import getpass
from pathlib import Path

def main():
    print("=" * 50)
    print("SYSTEM INFORMATION")
    print("=" * 50)
    
    # Show current OS user
    print(f"\n📁 Current User: {getpass.getuser()}")
    
    # List current directory
    print(f"\n📂 Current Directory: {os.getcwd()}")
    print("Contents:")
    try:
        for item in sorted(os.listdir('.')):
            if os.path.isdir(item):
                print(f"  📁 {item}/")
            else:
                print(f"  📄 {item}")
    except PermissionError:
        print("  ❌ Permission denied")
    
    # List home directory
    home_dir = Path.home()
    print(f"\n🏠 Home Directory: {home_dir}")
    print("Contents:")
    try:
        for item in sorted(os.listdir(home_dir)):
            if os.path.isdir(home_dir / item):
                print(f"  📁 {item}/")
            else:
                print(f"  📄 {item}")
    except PermissionError:
        print("  ❌ Permission denied")
    
    # Show environment variables
    print(f"\n🌍 Environment Variables:")
    print("-" * 30)
    for key, value in sorted(os.environ.items()):
        # Truncate very long values for readability
        if len(value) > 80:
            value = value[:77] + "..."
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
