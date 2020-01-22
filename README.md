# Git commit strategy

1. Branch to a 'featureBranch'
2. Do your ugly little commits
3. Do

```bash
git checkout master
git merge --squash feature/bugfix
git commit
```
