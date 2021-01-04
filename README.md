# Usage

To Install this package. Use :
```
  pip install pathsolver
```
To launch the application :
```
  from pathsolver import solve

  maze = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

  start = (5, 3)
  end = (2, 2)

  output, path = solve(maze, start, end)

```
<dl>Credits: Nicholas-Swift (https://gist.github.com/Nicholas-Swift/003e1932ef2804bebef2710527008f44)</dl>
<dl>Visit our GitHub Repository for more information: https://github.com/toshihiroryuu/PyPi--Package---pathsolver</dl>
