# 163-MV

本仓库存储 163 mv 项目的前端需要的库

可以解析全网易云的 mv

本项目和 [zkeq/163MV-Python-FastAPI](https://github.com/zkeq/163MV-Python-FastAPI) 配合使用

- API 的示例地址为 https://163.icodeq.com

- 使用具体方法参见：[归档 | 全自动解析 微博/微信 视频](https://icodeq.com/2022/03e4ec0968c8/)

```python
https://163.icodeq.com/?vid={vid}
```

### 搭建步骤

1. 修改 `/api/163mv/index.py` 中的 `Redis` 地址（只需要填地址和端口号）

2. 将第 `23` 行的对接地址填成你自己部署的后端

3. 即改这个：`url = 'https://163mv.icodeq.com/?vid={vid}'.format(vid=vid)`

4. 将项目推送至 `vercel`

5. 在 `vercel` 的环境变量中添加 

6. 键名为： `PASSWORD` ，值为你 `Redis` 密码的一条数据

7. 重新部署即可使用 