这是我的博客，站点列表：

- https://hexo.wenyuanhome.top
- https://lankning.github.io
- https://lankning.gitee.io

推送帮助：

1. 添加仓库

```bash
git remote add gitee https://gitee.com/lankning/lankning.git
git remote add gogs http://git.wenyuanhome.top/lankning/lankning.git
git remote add github https://github.com/lankning/lankning.github.io.git
```

2. 推送

```bash
git add .
git commit -m "update"
git push -u gitee master
git push -u gogs master
git push -u github master
```

参考：

1. [git多个远程仓库 - 铁芒箕 - 博客园 (cnblogs.com)](https://www.cnblogs.com/bwar/p/9297343.html)