# 月光博客 Hugo 项目目录说明

本项目是从 Z-Blog ASP 迁移到 Hugo 的多分区个人博客（月光博客），使用自定义布局（非第三方主题）。

---

## 根目录

| 路径 | 类型 | 用途 |
|------|------|------|
| `.git/` | 目录 | Git 版本控制仓库数据 |
| `.gitignore` | 文件 | Git 忽略规则（忽略 `content/`、`public/`、`static/`、`*.mdb`、`mdb/`） |
| `hugo.toml` | 文件 | Hugo 主配置文件：站点标题、URL、分类法、分页、输出格式等 |
| `gen_aliases.py` | 文件 | 构建后补丁脚本，生成旧 `.html` 链接的跳转页（详见下文「构建后补丁」） |
| `archetypes/` | 目录 | 内容原型模板，新建文章时的默认 front matter |
| `content/` | 目录 | 网站全部内容：文章、分类页、标签页、归档页 |
| `data/` | 目录 | 站点数据配置（JSON），供模板读取 |
| `layouts/` | 目录 | 网站模板（自定义 HTML 布局） |
| `static/` | 目录 | 静态资源（图片、CSS、logo），构建时原样复制到站点根目录 |
| `public/` | 目录 | Hugo 构建产物，运行 `hugo` 后生成，已被 Git 忽略，可随时删除重建 |

---

## archetypes/ — 内容原型

| 文件 | 用途 |
|------|------|
| `default.md` | 默认文章原型模板，定义新建文章时的 front matter（日期、草稿状态、标题） |

---

## content/ — 网站内容

### 文章分区（Section）

每个分区对应一个独立的博客子站，有各自的首页、分类、归档。

| 目录 | 分区名称 | 说明 |
|------|----------|------|
| `archives/` | 全站归档 | 所有文章的统一归档列表 |
| `apps/` | 移动应用观察 | iPhone / iPad / Android 应用评论 |
| `book/` | 短篇小说 | 经典短篇小说 |
| `google/` | 谷歌地图观察 | 谷歌地图/地球相关内容 |
| `info/` | 网站运营优化 | 建站、SEO、服务器、运营等 |
| `movie/` | 电影评论 | 欧美、日韩、港台、大陆电影影评 |
| `weibo/` | 月光微博客 | 微博客短文 |
| `xiaoshuo/` | 长篇小说 | 长篇小说连载 |

### 主博客分类法

| 目录 | 分类法 | 说明 |
|------|--------|------|
| `categories/` | 主分类 | 编程开发、互联网络、软件应用、生活感悟、搜索引擎、网络地图、网络日志、网站建设、业界动态 |
| `tags/` | 主标签 | 主博客的标签集合 |

### 各分区专属分类法

命名规则：`<分区名>_categories`（分类）或 `<分区名>_tags`（标签）。

| 目录 | 所属分区 | 类型 |
|------|----------|------|
| `apps_tags/` | 移动应用 | 标签 |
| `book_categories/` | 短篇小说 | 分类 |
| `google_categories/` | 谷歌地图 | 分类 |
| `google_tags/` | 谷歌地图 | 标签 |
| `info_categories/` | 网站运营 | 分类 |
| `movie_categories/` | 电影评论 | 分类 |
| `weibo_categories/` | 微博客 | 分类 |
| `weibo_tags/` | 微博客 | 标签 |

> 每个分区目录下通常还有一个 `archives/` 子目录，用于存放该分区的归档页。

---

## data/ — 站点数据配置

| 文件 | 用途 |
|------|------|
| `site.json` | 各分区的标题与导航菜单配置（名称 + URL） |
| `taxonomy.json` | 分类/标签的中文名到 URL slug 的映射（如"编程开发" → `program`） |
| `catorder.json` | 各分区分类的显示顺序数组 |
| `logos.json` | 分类标识到 logo 图标文件名的映射（对应 `static/logo/` 下的 gif 文件） |

---

## layouts/ — 模板布局

本项目使用完全自定义的 HTML 模板，未使用第三方主题。

### `_default/` — 默认模板

| 文件 | 用途 |
|------|------|
| `baseof.html` | 基础骨架模板，定义页面整体 HTML 结构 |
| `list.html` | 列表页模板，用于分类页、标签页、归档页、分区首页 |
| `single.html` | 单篇文章页模板 |

### `partials/` — 可复用模板片段

| 文件 | 用途 |
|------|------|
| `ctx.html` | 上下文变量计算（分区、分类等公共逻辑） |
| `head.html` | HTML `<head>` 部分（meta、样式、脚本引用） |
| `header.html` | 页头与导航栏 |
| `footer.html` | 页脚 |
| `sidebar.html` | 侧边栏 |
| `pagination.html` | 分页组件 |

---

## static/ — 静态资源

构建时原样复制到站点根目录，URL 路径与目录结构一致。

| 目录/文件 | 用途 |
|-----------|------|
| `images/` | 站点通用图片：favicon、apple-touch-icon、二维码、RSS/邮件订阅图标 |
| `logo/` | 各分类对应的 logo 图标（gif 格式），由 `data/logos.json` 映射引用 |
| `theme/style.css` | 站点主样式表 |
| `theme/images/` | 主题界面图标：箭头、作者、分类、评论、日期、永久链接、搜索、浏览量等 |

---

## 构建后补丁：gen_aliases.py

### 用途

本项目的分类页和标签页使用**目录式 URL**（如 `/cat/tech/`），这样才能让分页呈现为 `/cat/tech/page/2/`。但原 Z-Blog 站点和搜索引擎收录的链接是 `.html` 形式（如 `/cat/tech.html`、`/cat/tech_2.html`）。

`gen_aliases.py` 在 Hugo 构建完成后运行，扫描 `public/` 目录，为每个目录式页面生成对应的旧式 `.html` 跳转桩页，实现旧链接兼容。

### 跳转映射规则

| 旧链接（Z-Blog 形式） | 新链接（Hugo 目录式） |
|----------------------|---------------------|
| `/cat/tech.html` | `/cat/tech/` |
| `/movie/tag/Romance.html` | `/movie/tag/Romance/` |
| `/cat/tech_2.html` | `/cat/tech/page/2/` |
| `/movie/tag/Romance_5.html` | `/movie/tag/Romance/page/5/` |
| `/page/index_2.html` | `/page/2/` |
| `/apps/page/index_3.html` | `/apps/page/3/` |

覆盖的分区：主站、`weibo`、`google`、`apps`、`info`、`movie`。

### 生成的桩页内容

每个桩页是一个极简 HTML，通过 meta refresh 立即跳转，并声明 canonical 指向新地址：

```html
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/cat/tech/"><link rel="canonical" href="https://www.williamlong.info/cat/tech/"></head><body><a href="/cat/tech/">跳转</a></body></html>
```

全站合计生成约 1242 个跳转页。

### 使用方式

**必须每次构建后运行**，因为它依赖 `public/` 中实际生成的分页目录结构：

```bash
hugo
python gen_aliases.py
```

脚本会输出生成数量：

```
alias pages generated: 1242
```

### 注意事项

- 脚本中的 `PUB` 常量写死了绝对路径 `e:\hugo\williamlong\public`，换机器或换路径时需要修改。
- 如果清空 `public/` 后重新构建但**没有**重跑本脚本，所有旧 `.html` 链接将变成 404，会影响搜索引擎收录和外部引用。
- 若站点仅本地预览、不对外发布，可删除本脚本，直接使用目录式 URL 访问即可。

---

## 常用命令

```bash
# 本地预览（开发模式，带热重载）
hugo server --port 1313 --bind 127.0.0.1

# 构建生产站点（输出到 public/）
hugo

# 构建并生成旧链接跳转页（完整发布流程）
hugo
python gen_aliases.py

# 清理构建产物
Remove-Item public -Recurse -Force
```
