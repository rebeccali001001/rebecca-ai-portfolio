# Unsupervised Learning

- Module: 01 · AI Foundations
- Topic: Unsupervised Learning
- Source File: `unsupervised-learning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Unsupervised Learning | 无监督学习 | Learning from data without given labels | 没有人提前告诉机器每条数据的答案，机器自己找规律 |
| Unsupervised learning | 无监督学习 | A machine-learning method that finds structure | 一种让机器从没有标签的数据里找结构的方法 |
| machine-learning method | 机器学习方法 | A way for a machine-learning system to learn | 机器学习系统学习的一种方式 |
| unlabeled data | 无标签数据 | Data without predefined answers or names | 没有标注正确类别的数据 |
| predefined labels | 预先定义的标签 | Labels decided before learning | 在训练前就写好的分类答案 |
| correct answer | 正确答案 | The expected answer for an example | 每条训练例子对应的标准答案 |
| example | 示例 | One item used for learning or comparison | 数据中的一条例子 |
| data | 数据 | Information given to a system | 提供给系统的信息 |
| structure | 结构 | An organization or pattern in data | 数据里面隐藏的组织方式或规律 |
| similar groups | 相似群组 | Groups containing similar items | 把相像的东西放在一起 |
| patterns | 模式 / 规律 | Repeated or meaningful regularities | 数据中反复出现的规律 |
| relationships | 关系 | Connections between data items or features | 数据项之间的联系 |
| unusual data points | 异常数据点 | Data items that look different from others | 和大多数数据不一样的点 |
| clustering algorithm | 聚类算法 | An algorithm that forms groups of similar items | 自动把相似数据分组的算法 |
| clustering | 聚类 | Grouping items by similarity | 按相似程度分组 |
| cluster | 簇 / 聚类组 | A mathematical group of similar data points | 算法认为相似的一组数据 |
| group | 组 / 群组 | A collection of related items | 放在一起的一批数据 |
| group names | 群组名称 | Human-readable names assigned to groups | 人后来给数据组起的名字 |
| human names | 人类命名 | Names people assign to discovered groups | 机器发现组后，人类给它们贴的名称 |
| cat | 猫 | An example of a human concept label | “猫”这种人类理解的类别名 |
| dog | 狗 | An example of a human concept label | “狗”这种人类理解的类别名 |
| sorting a mixed box | 整理混合箱子的类比 | Sorting objects without labels | 像整理一箱没有标签的杂物 |
| mixed box | 混合箱 | A collection of mixed objects | 混在一起、没有分类的东西 |
| labels | 标签 | Names or categories attached to data | 给数据写上的类别或答案 |
| similarities | 相似性 | Ways in which items resemble each other | 两个数据看起来相像的地方 |
| measure patterns | 衡量模式 | Compare data using measurable properties | 用可以测量的特征比较数据 |
| similarity | 相似度 | A measure of how alike two items are | 两个数据有多像的数值或判断 |
| measurable features | 可测量特征 | Properties that can be compared numerically | 可以拿来比较的属性，例如大小或频率 |
| feature | 特征 | A measurable property of an item | 描述一条数据的一个属性 |
| recurring patterns | 重复出现的模式 | Patterns that appear again and again | 反复出现的规律 |
| find structure | 发现结构 | Detect organization in data | 找到数据自然形成的组织方式 |
| create groups | 创建群组 | Form groups from data | 根据规律把数据分成几组 |
| representations | 表示 / 表征 | A form used to represent data | 用另一种形式表示原始数据 |
| compact representations | 紧凑表征 | Smaller representations that retain useful structure | 用更少的信息保留重要规律 |
| inspect results | 检查结果 | Look at discovered groups or patterns | 人查看机器找出的结果 |
| interpret results | 解释结果 | Decide what the discovered structure means | 人判断这些分组到底代表什么 |
| useful structure | 有用结构 | A discovered pattern that helps a task | 对实际任务有帮助的规律 |
| people interpret | 人类解释 | People assign meaning to machine output | 机器输出后由人来理解它的含义 |
| customer segmentation | 客户分群 | Divide customers by similar behavior | 按使用习惯把客户分成几类 |
| customer behavior | 客户行为 | How customers use or act | 客户的使用和行动方式 |
| usage patterns | 使用模式 | Repeated patterns in usage | 用户使用产品时反复出现的习惯 |
| customer groups | 客户群组 | Groups of customers with similar behavior | 行为相似的客户集合 |
| document grouping | 文档分组 | Group documents with similar patterns or topics | 把主题相近的文档放到一起 |
| document | 文档 | A piece of written information | 一份文字资料 |
| documents | 文档集合 | Multiple pieces of written information | 多份文字资料 |
| topics | 主题 | Main subjects discussed in data | 文档主要在讲什么 |
| similar topics | 相似主题 | Topics that are alike | 内容方向相近的主题 |
| anomaly discovery | 异常发现 | Finding unusual examples | 找出不寻常的数据 |
| anomaly detection | 异常检测 | Detecting data that differs from normal patterns | 判断哪些数据偏离正常情况 |
| normal activity patterns | 正常活动模式 | Patterns describing ordinary behavior | 平时正常活动的规律 |
| unusual examples | 异常示例 | Examples that do not fit common patterns | 不符合大多数规律的例子 |
| anomalies | 异常 | Unusual or unexpected data points | 和正常情况明显不同的数据 |
| possible anomalies | 可能的异常 | Items that may need investigation | 可能有问题、值得进一步查看的数据 |
| supervised learning | 监督学习 | Learning from examples with known labels | 训练例子带有正确答案的学习方式 |
| Supervised Learning | 监督学习 | A labeled learning setup | 使用标签学习的机器学习分支 |
| Reinforcement Learning | 强化学习 | Learning actions from feedback and rewards | 通过行动、反馈和奖励学习 |
| reinforcement learning | 强化学习 | A different way for systems to learn | 与无监督学习不同的学习方法 |
| Deep Learning | 深度学习 | A machine-learning approach often using many neural layers | 常用多层神经网络的机器学习方法 |
| Artificial Intelligence | 人工智能 | The broad field of intelligent-looking machines | 让机器完成看起来有智能任务的广泛领域 |
| Machine Learning | 机器学习 | Learning patterns from data | 让机器从数据中学规律 |
| taxonomy | 分类体系 | A hierarchy of related concepts | 把概念按层级组织起来的体系 |
| learning approach | 学习方式 | A general way a system learns | 系统学习时采用的路线 |
| learning setup | 学习设置 | The information and feedback available during learning | 学习时系统能得到什么数据和反馈 |
| data point | 数据点 | One item or observation in a dataset | 数据集中的一条记录 |
| observation | 观测值 | One recorded case | 一次记录到的对象或情况 |
| sample | 样本 | One example from a dataset | 数据集中的一条样本 |
| dataset | 数据集 | A collection of data points | 一批数据的集合 |
| feature space | 特征空间 | A space described by measurable features | 用特征表示数据位置的空间 |
| distance metric | 距离度量 | A rule for measuring difference | 判断两个数据相差多少的规则 |
| similarity measure | 相似度量 | A rule for measuring likeness | 判断两个数据有多像的规则 |
| cluster assignment | 聚类分配 | Choosing a cluster for a data point | 决定一条数据属于哪一组 |
| centroid | 质心 | A representative center of a cluster | 一组数据的代表中心 |
| density | 密度 | How many points occupy a region | 某个区域里数据点有多集中 |
| outlier | 离群点 | A point far from the usual pattern | 远离大多数数据的点 |
| latent representation | 潜在表征 | A hidden useful representation learned from data | 数据中学出来但原本看不见的表示 |
| embedding | 嵌入 / 向量表征 | A numerical representation of an item | 把数据变成可比较的数字向量 |
| vector | 向量 | An ordered list of numbers | 一串有顺序的数字，用来表示数据 |
| dimensionality reduction | 降维 | Represent data with fewer dimensions | 用更少的维度表示数据 |
| training | 训练 | Learning patterns from available examples | 让模型从数据中学习规律的过程 |
| training data | 训练数据 | Data used to learn patterns | 用来训练模型的数据 |
| model | 模型 | A learned system that captures patterns | 学完规律后可以处理新数据的系统 |
| inference | 推理 / 推断 | Applying a learned model to new data | 用已经学会的模型处理新数据 |
| new input | 新输入 | Data the model has not seen in the same form | 交给模型处理的新数据 |
| prediction | 预测 | An output produced for new data | 模型对新数据给出的结果 |
| evaluation | 评估 | Checking whether a result is useful or reliable | 检查模型结果好不好、有没有用 |
| cluster validation | 聚类验证 | Checking whether discovered clusters are meaningful | 检查分出来的组是否合理 |
| silhouette score | 轮廓系数 | A score for separation and cohesion of clusters | 衡量组内相似、组间分开的指标 |
| Davies–Bouldin index | Davies–Bouldin 指数 | A cluster-quality index based on similarity between clusters | 衡量聚类质量的指标，通常越小越好 |
| Calinski–Harabasz index | Calinski–Harabasz 指数 | A cluster-quality index using between- and within-cluster dispersion | 用组间和组内分散程度衡量聚类质量 |
| elbow method | 肘部法则 | Choose a cluster count from diminishing gains | 看曲线拐点来选择分几组 |
| k-means | k-均值聚类 | Iteratively assign points to k centers | 反复把数据分到若干中心附近 |
| hierarchical clustering | 层次聚类 | Build a tree of nested groups | 逐层合并或拆分数据组 |
| dendrogram | 树状图 | A tree showing hierarchical clusters | 展示层次聚类关系的树形图 |
| DBSCAN | DBSCAN 密度聚类 | Find dense regions and mark sparse points as noise | 按密度找群组，也能识别噪声点 |
| Gaussian mixture model | 高斯混合模型 | Model data as a mixture of Gaussian distributions | 假设数据由多个高斯分布混合而成 |
| mixture model | 混合模型 | A model combining several component distributions | 用多个分布共同描述数据 |
| density estimation | 密度估计 | Estimate where data is concentrated | 估计数据在各处有多密集 |
| principal component analysis | 主成分分析 | Find directions that preserve major variation | 找出最能保留变化信息的方向 |
| PCA | PCA / 主成分分析缩写 | Short name for principal component analysis | 主成分分析的常用缩写 |
| manifold learning | 流形学习 | Learn a lower-dimensional shape in data | 找到高维数据背后的低维形状 |
| autoencoder | 自编码器 | Encode and reconstruct data through a model | 把数据压缩后再尽量还原的模型 |
| reconstruction | 重构 | Rebuild an input from a representation | 从压缩表示还原原始数据 |
| topic modeling | 主题建模 | Discover topics in a collection of documents | 自动发现一批文档中的主题 |
| association rule | 关联规则 | A pattern showing items that occur together | 发现哪些项目经常一起出现的规则 |
| market-basket analysis | 购物篮分析 | Analyze items bought together | 分析顾客经常一起购买什么 |
| generative modeling | 生成建模 | Learn a data distribution to generate examples | 学会数据分布并生成新例子 |
| self-supervised learning | 自监督学习 | Create learning signals from the data itself | 从数据自身制造训练信号 |
| data preprocessing | 数据预处理 | Prepare data before learning | 在学习前清理和整理数据 |
| normalization | 归一化 | Put values on a comparable scale | 把不同范围的数值调整到可比较范围 |
| scaling | 缩放 | Rescale feature values | 改变特征数值尺度 |
| noise | 噪声 | Irrelevant or random variation in data | 数据里的杂乱或随机成分 |
| data quality | 数据质量 | How complete, consistent, and useful data is | 数据是否完整、可靠、适合使用 |
| interpretability | 可解释性 | How understandable the result is to people | 人能不能理解模型为什么这样分组 |
| human review | 人工复核 | People check or interpret the output | 由人检查机器结果是否合理 |
| deployment | 部署 | Put a model into a real system | 把模型放进真实应用中运行 |
| monitoring | 监控 | Watch model behavior after deployment | 上线后持续观察模型表现 |
| data drift | 数据漂移 | The input data distribution changes over time | 现实数据变了，和训练时不一样了 |
| model drift | 模型漂移 | Model usefulness changes over time | 模型效果随着环境变化而下降 |
| privacy | 隐私 | Protection of information about people | 防止用户数据被不当暴露 |
| sensitive data | 敏感数据 | Data that needs extra protection | 泄露后可能造成伤害的数据 |
| anomaly alert | 异常告警 | A notification about a possible unusual event | 发现异常后提醒人处理 |
| raw data | 原始数据 | Data before processing | 还没有清洗或转换的数据 |
| structured data | 结构化数据 | Data organized into fields or columns | 按固定字段整理的数据 |
| unstructured data | 非结构化数据 | Data without a fixed table-like format | 没有固定表格结构的文字、图片等数据 |
| mathematical grouping | 数学分组 | A group formed by numerical rules | 按数字规律分出来的组 |
| human concept | 人类概念 | A meaning or category people recognize | 人脑理解的类别或含义 |
| automatic human understanding | 自动人类理解 | The ability to truly understand human meaning | 机器自动懂得人类概念，不等于分组 |
| useful meaning | 有用含义 | Meaning assigned for a task | 对实际任务有帮助的解释 |
| correct labels in advance | 事先正确标签 | Known answers supplied before learning | 训练前就给机器的标准分类答案 |
| measurable pattern | 可测量模式 | A pattern detectable through features | 能通过数据特征测出来的规律 |
| group interpretation | 群组解释 | Human explanation of a discovered group | 人给算法分组赋予的解释 |
| pattern discovery | 模式发现 | Finding regularities without predefined targets | 不预设答案而发现规律 |
| representation learning | 表征学习 | Learn useful representations from data | 自动学出适合后续任务的数据表示 |

## Potential Missing Concepts

- K-medoids, mean shift, spectral clustering, affinity propagation, and fuzzy c-means: additional clustering methods not named in the page.
- Hierarchical agglomerative clustering, divisive clustering, linkage criteria, and dendrogram cutting: details needed to explain hierarchical clustering.
- DBSCAN parameters `eps` and `minPts`, core point, border point, and noise point: operational details for density-based clustering.
- Gaussian mixture model, expectation-maximization (EM), soft assignment, and probability density: probabilistic clustering concepts.
- Principal Component Analysis (PCA), t-SNE, and UMAP: common dimensionality-reduction methods for visualization or compact representation.
- Autoencoder, variational autoencoder (VAE), encoder, decoder, bottleneck, and reconstruction loss: representation-learning concepts.
- Topic modeling methods such as Latent Dirichlet Allocation (LDA), topic-word distribution, and document-topic distribution.
- Association rules, support, confidence, and lift: measures for co-occurrence discovery.
- Density estimation, kernel density estimation (KDE), and probability distribution: non-clustering structure discovery.
- Distance functions such as Euclidean distance, Manhattan distance, cosine similarity, and Mahalanobis distance.
- Feature engineering, feature selection, missing values, categorical encoding, and outlier handling.
- Standardization, min-max scaling, normalization, and the effect of feature scale on distance-based methods.
- Hyperparameters, number of clusters (`k`), initialization, random seed, convergence, and local optimum.
- Hard clustering versus soft clustering; membership probability and overlapping clusters.
- Internal validation, external validation, ground truth, and stability analysis.
- Silhouette analysis, elbow plot, Davies–Bouldin Index, Calinski–Harabasz Index, and gap statistic.
- Cluster interpretability, cluster profiling, naming clusters, and human-in-the-loop review.
- Anomaly detection methods such as isolation forest, one-class SVM, local outlier factor (LOF), and robust covariance.
- Novelty detection, concept drift, data drift, threshold selection, false positives, and false negatives.
- Self-supervised learning, contrastive learning, pretext task, and pseudo-labels: related but distinct ways to obtain learning signals without manual labels.
- Generative modeling, latent variable, likelihood, sampling, and synthetic data generation.
- Embedding space, vector representation, nearest-neighbor search, and semantic similarity.
- Curse of dimensionality, sparsity, manifold hypothesis, and hubness in high-dimensional data.
- Data leakage, privacy risk, sensitive attributes, fairness, proxy features, and harmful segmentation.
- Reproducibility, random initialization, model versioning, experiment tracking, and deployment monitoring.
- Cluster drift, retraining, alert thresholds, rollback, and human escalation for production anomaly systems.

## Aliases / Synonyms

- Unsupervised Learning / unsupervised learning / unsupervised machine learning / unlabeled-data learning
- Unlabeled data / unlabelled data / data without labels / data without predefined answers
- Clustering / cluster analysis / grouping / unsupervised grouping
- Cluster / group / segment / cohort / discovered class
- Similarity / likeness / proximity / closeness
- Anomaly / outlier / unusual example / abnormal observation / novelty
- Anomaly discovery / anomaly detection / outlier detection / novelty detection
- Customer segmentation / customer clustering / audience segmentation / user grouping
- Document grouping / document clustering / text clustering / topic grouping
- Representation / data representation / feature representation / latent representation
- Embedding / vector representation / numerical representation / learned representation
- Dimensionality reduction / dimension reduction / feature compression / low-dimensional projection
- Principal Component Analysis / Principal Components Analysis / PCA
- Gaussian Mixture Model / Gaussian mixture / GMM
- Self-supervised learning / self-supervision / learning from self-generated targets
- Noise / random variation / irrelevant variation / measurement noise
- Human interpretation / human review / expert inspection / human-in-the-loop analysis

## Do Not Confuse Candidates

- Unsupervised Learning vs Supervised Learning: unsupervised learning looks for structure without predefined labels; supervised learning learns from labeled examples with known answers.
- Unsupervised Learning vs Reinforcement Learning: unsupervised learning discovers structure in data; reinforcement learning learns actions through interaction, feedback, and rewards.
- Unsupervised Learning vs Machine Learning: unsupervised learning is one learning approach inside the broader machine-learning field.
- Unsupervised Learning vs Deep Learning: deep learning is a model/learning approach often based on multi-layer neural networks, while unsupervised learning describes the availability of labels and learning setup.
- Unsupervised Learning vs Artificial Intelligence: artificial intelligence is the broad field; unsupervised learning is one method within machine learning.
- Cluster vs human concept: a cluster is a mathematical grouping; it does not automatically mean “cat,” “dog,” customer type, or another human category.
- Cluster vs class: a discovered cluster is not necessarily a ground-truth class supplied by people.
- Similarity vs identity: two items can be similar without being the same item.
- Similarity measure vs distance metric: similarity increases with likeness, while distance usually increases with difference; implementations may convert one into the other.
- Anomaly vs error: an unusual point may be valid data, not necessarily a data-entry mistake.
- Anomaly detection vs supervised classification: anomaly detection can work without labeled normal/abnormal examples; classification learns from labeled categories.
- Unlabeled data vs unstructured data: unlabeled means no target labels; unstructured means the data does not have a fixed tabular format.
- Embedding vs meaning: an embedding is a model-generated numerical representation, not meaning itself.
- Embedding vs database: an embedding is a vector; a database stores vectors, metadata, or records.
- Embedding vs keyword: an embedding compares learned patterns or relationships, while a keyword is a literal word or phrase match.
- Dimensionality reduction vs feature selection: dimensionality reduction transforms features into fewer dimensions; feature selection keeps a subset of original features.
- Clustering vs dimensionality reduction: clustering creates groups; dimensionality reduction creates a compact representation or projection.
- PCA vs clustering: PCA finds directions of variation; it does not by itself assign cluster labels.
- k-means vs the meaning of k: `k` is a chosen number of clusters, not a discovered human truth.
- Hard clustering vs soft clustering: hard clustering assigns one group; soft clustering can assign membership probabilities to multiple groups.
- Noise vs outlier: noise is unwanted variation; an outlier is an observation that appears unusual, and it may be meaningful.
- Human interpretation vs automatic human understanding: a model can produce groups without understanding the human meaning people later assign to them.
- Pattern discovery vs random grouping: unsupervised grouping uses measurable patterns or similarity; it is not arbitrary random sorting.
- Training vs inference: training learns patterns from available data; inference applies a learned model to new data.
- Evaluation vs interpretation: evaluation checks quality or usefulness; interpretation explains what a discovered group might mean.
- Self-supervised learning vs unsupervised learning: self-supervised learning creates a training signal from the data itself and may use predictive objectives, while unsupervised learning is the broader label-free family.
- Association rule vs correlation: an association rule describes co-occurrence; it does not automatically prove causation.
- Data drift vs model drift: data drift is a change in inputs; model drift is a change in usefulness or performance.

## Notes

- The source page defines unsupervised learning as a machine-learning method that learns from unlabeled data and finds patterns or structure without predefined labels.
- The page explicitly names similar groups, patterns, relationships, unusual data points, clustering, compact representations, customer segmentation, document grouping, and anomaly discovery.
- The page’s process is: collect unlabeled data → measure patterns or similarity → find structure → create groups or representations → inspect results.
- The page emphasizes that group names do not automatically come from the algorithm; people interpret whether discovered structure is useful.
- The page contrasts unsupervised learning with supervised learning and random grouping, and separates a mathematical cluster from a human concept.
- The AI Foundations overview places Unsupervised Learning under Machine Learning alongside Supervised Learning, Reinforcement Learning, and Deep Learning.
- The related-concepts line on the source page names Clustering, Embeddings, and Dimensionality reduction; the Embeddings page further frames an embedding as a numerical vector representation that can be compared.
- The source examples are customer behavior → customer groups, documents → similar topics, and normal activity patterns → possible anomalies.
- The source includes a video section with English captions at `vedio/unsupervised-learning.mp4` and `vedio/unsupervised-learning.vtt`; this is media context, not a glossary concept.
- Raw collection intentionally preserves repeated terms and overlapping candidates. No deduplication or pruning was performed.
