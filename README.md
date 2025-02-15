# wc Tool in Python
[Problem Statement link](https://codingchallenges.fyi/challenges/challenge-wc/)
``` 
Environment: Linux
```

### Steps to create Symlink (Soft Copy)
When creating the CLI with just `Python`, we can run it as:
`python3 ccwc.py -c test.txt`.

However, to create a __CLI tool__ that runs globally like a system command (`ccwc`) instead of running it with `python3 ccwc.py`, we follow the following approach:

1. Add a shebang to `ccwc.py`: `#!/usr/bin/env python3`
2. Make the script executable: `chmod +x ccwc.py` (so that we can now run `./ccwc.py -c test.txt`)
3. We __Symlink__ the Script to a Directorylisted in our system's `$PATH`: `ln -s /path/to/ccwc.py ~/.local/bin/ccwc`
> A **symlink** (short for symbolic link) is a special type of file that acts as a pointer to another file or directory. It works like a shortcut in Windows but is more powerful because the system treats it as if it were the actual file.

> Types of links in Linux:
> * Hard Link: 
>      - A hard link is another name for the same file.
>      - It points to the same inode (actual file data) on the disk.
>      - If you delete the original file, the hard link still works.
> * Soft Link (Symlink): 
>      - A soft link is just a pointer (shortcut) to the original file.
>      - If you delete the original file, the symlink breaks (it points to nothing).

4. We verify and use our command: `ccwc -c test.txt`