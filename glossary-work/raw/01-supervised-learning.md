# Topic

Supervised Learning

- Module: 01 · AI Foundations
- Topic: Supervised Learning
- Source File: `supervised-learning.html`
- Module/Topic/Source File: `01 · AI Foundations / Supervised Learning / supervised-learning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Supervised Learning | 监督学习 | Learning from examples that include correct answers | 给模型看带答案的例子，让它学会回答新问题 |
| Machine Learning | 机器学习 | A way for computers to learn patterns from data | 让电脑从数据里找规律，而不是把每条规则都手写出来 |
| Artificial Intelligence | 人工智能 | The broad field of machines doing tasks that seem intelligent | 让机器完成看起来需要智能的事情的大领域 |
| learning method | 学习方法 | A way a model learns from data | 模型学习数据规律的一种方式 |
| learning setup | 学习设置 | The arrangement of data and feedback used for learning | 规定模型用什么数据、什么反馈来学习 |
| labeled example | 带标签的示例 | An example paired with its correct answer | 一个和正确答案配在一起的例子 |
| labeled data | 标注数据 | Data with known labels or target answers | 已经有人标出答案的数据 |
| label | 标签 | The known category or answer for an example | 告诉模型“这是什么”的答案 |
| target | 目标值 | The answer the model is supposed to predict | 模型要预测的目标答案 |
| target answer | 目标答案 | The correct answer attached to an input | 和输入配对的正确答案 |
| correct answer | 正确答案 | The expected answer used for learning or checking | 用来教模型或检查模型的标准答案 |
| input | 输入 | The information given to the model | 送进模型的数据 |
| new input | 新输入 | Data the model has not seen as the same training example | 需要模型实际处理的新数据 |
| example | 示例 | One data case used for learning or checking | 数据中的一个具体案例 |
| training example | 训练示例 | An input-answer pair used during training | 训练时给模型练习的一组输入和答案 |
| input-output pair | 输入输出对 | An input matched with its expected output | 输入和应该得到的结果的一对数据 |
| feature | 特征 | A measurable property used by a model | 描述对象、帮助模型判断的一个属性 |
| feature vector | 特征向量 | A numeric list representing an example's features | 把一个例子的多个特征排成数字列表 |
| dataset | 数据集 | A collection of examples | 一批用于训练或测试的数据 |
| training data | 训练数据 | Data used to fit the model | 用来教模型的那部分数据 |
| held-out data | 留出数据 | Data kept aside for checking the model | 训练时先不让模型看的检查数据 |
| test data | 测试数据 | Data used for a final or independent check | 用来最后检验模型表现的数据 |
| validation data | 验证数据 | Data used to tune choices and check progress | 用来调参数和比较方案的数据 |
| train-validation-test split | 训练集-验证集-测试集划分 | Dividing data into training, tuning, and final-check sets | 把数据分成学习、调试、最后验收三份 |
| data split | 数据划分 | Separating data for different stages | 按用途把数据分组 |
| representative data | 有代表性的数据 | Data that reflects the cases seen in real use | 能代表真实使用情况的数据 |
| trustworthy target answers | 可信的目标答案 | Reliable answers used as labels | 质量可靠、值得信任的标准答案 |
| annotation | 标注 | The act of attaching labels to data | 给数据加上答案或类别的过程 |
| data labeling | 数据标注 | Creating labels for examples | 为训练例子制作标签 |
| label quality | 标签质量 | How accurate and consistent labels are | 标签是否准确、统一、可靠 |
| ground truth | 真实标签 / 基准真值 | The best available reference answer | 用来对照模型结果的可信标准答案 |
| noisy label | 噪声标签 | A label that is wrong, vague, or inconsistent | 错了、模糊了或前后不一致的标签 |
| class | 类别 | One possible category in a classification task | 分类任务中的一种可能类别 |
| category | 类别 | A group or label an example can belong to | 把对象归入的某一类 |
| binary classification | 二分类 | Choosing between two classes | 只能在两类中选一类 |
| multiclass classification | 多分类 | Choosing one of several classes | 在多个类别中选一个 |
| multilabel classification | 多标签分类 | Assigning several labels to one example | 一个例子可以同时属于多个类别 |
| classification | 分类 | Predicting a category or label | 预测“它属于哪一类” |
| regression | 回归 | Predicting a numeric value | 预测一个数值，比如价格 |
| numerical value | 数值 | A quantity expressed as a number | 用数字表示的量 |
| continuous value | 连续值 | A value that can vary along a range | 可以在一个范围内连续变化的数 |
| discrete class | 离散类别 | A choice from separate categories | 从互不连续的类别中选择 |
| prediction | 预测 | A model's answer for an input | 模型对输入给出的结果 |
| predicted answer | 预测答案 | The answer produced by the model | 模型实际输出的答案 |
| model output | 模型输出 | What the model returns | 模型返回的结果 |
| class prediction | 类别预测 | A predicted category | 模型判断出的类别 |
| predicted number | 预测数值 | A numeric prediction | 模型估计出来的数字 |
| probability | 概率 | A number expressing how likely something is | 表示某种结果可能性的数字 |
| predicted probability | 预测概率 | The model's estimated likelihood for an outcome | 模型认为某个结果有多可能 |
| confidence score | 置信度分数 | A score expressing model confidence | 模型对自己答案有多确信的分数 |
| risk score | 风险分数 | A score estimating risk | 表示风险高低的分数 |
| score | 分数 / 评分 | A numeric value used to rank or assess an input | 用数字表示判断结果或优先级 |
| ranking | 排名 / 排序 | Ordering items by a model's scores | 按模型分数把对象排先后 |
| forecast | 预测值 / 预报 | A prediction about a future value | 对未来情况的估计 |
| demand forecasting | 需求预测 | Predicting future demand | 估计未来会需要多少商品或服务 |
| spam filtering | 垃圾邮件过滤 | Classifying messages as spam or not spam | 判断邮件是不是垃圾邮件 |
| spam | 垃圾邮件 | An unwanted or suspicious message | 不想要的邮件 |
| not spam | 非垃圾邮件 | A normal wanted message | 正常、不是垃圾邮件的消息 |
| email | 电子邮件 | A message used as an example input | 作为输入案例的一封邮件 |
| credit risk | 信用风险 | The risk that a borrower will not repay | 借款人可能不还钱的风险 |
| financial history | 财务历史 | Past financial information about an applicant | 申请人过去的财务记录 |
| application | 申请资料 / 申请 | Information submitted for a decision | 用来申请贷款等服务的资料 |
| repayment outcome | 还款结果 | Whether and how a loan was repaid | 借款最后是否按时还款的结果 |
| demand | 需求 | The amount customers are likely to want | 客户可能想买或使用的数量 |
| past sales | 历史销售数据 | Previous sales records | 过去卖出了多少的记录 |
| price | 价格 | A value that may help predict demand | 可能影响需求预测的售价 |
| calendar data | 日历数据 | Time-related information such as dates or holidays | 日期、星期、节假日等时间信息 |
| future sales | 未来销售额 | Sales expected in a future period | 以后可能卖出的数量或金额 |
| new message | 新消息 | A message being classified after training | 训练完成后新收到的消息 |
| user input | 用户输入 | Information supplied by a user | 用户提供给系统的内容 |
| training | 训练 | Adjusting a model using examples | 让模型反复看数据并改进的过程 |
| model training | 模型训练 | The process of fitting a model to data | 用数据把模型教出来 |
| train | 训练模型 | To learn patterns from training data | 用训练数据学习规律 |
| inference | 推理 / 推断 | Applying a trained model to new data | 用已经学好的模型处理新数据 |
| prediction time | 预测阶段 | The time when the model produces an answer | 模型实际给出预测的阶段 |
| learned pattern | 学到的模式 | A regularity learned from examples | 模型从例子里学到的规律 |
| pattern | 模式 / 规律 | A repeated relationship in data | 数据中反复出现的关系 |
| model | 模型 | A learned system that maps inputs to outputs | 学会规律、能把输入变成输出的程序 |
| trained model | 训练好的模型 | A model after learning from data | 已经用数据训练完成的模型 |
| reusable model | 可复用模型 | A learned model that can be applied to new cases | 学好后可以反复处理新案例的模型 |
| internal value | 内部值 | A value inside the model that can be adjusted | 模型内部会被调整的数字 |
| parameter | 参数 | A learned internal value of a model | 模型训练中学出来的内部数字 |
| weight | 权重 | A parameter controlling the influence of a signal | 表示某个信息有多重要的内部数字 |
| bias | 偏置 | A learned offset that shifts a prediction | 帮模型整体调整结果位置的内部数字 |
| adjust internal values | 调整内部值 | Change learned values to improve predictions | 改模型内部数字，让预测更好 |
| reduce prediction errors | 减少预测错误 | Make predictions closer to correct answers | 让模型答案更接近标准答案 |
| prediction error | 预测误差 | The difference between prediction and target | 模型答案和正确答案之间的差距 |
| error | 错误 / 误差 | A wrong answer or distance from the target | 模型答错或偏离答案的程度 |
| loss | 损失 | A number measuring how bad predictions are | 用一个数字表示模型错得多不多 |
| loss function | 损失函数 | A rule for calculating prediction error | 计算模型预测有多差的规则 |
| objective function | 目标函数 | A quantity the training process tries to optimize | 训练时要尽量变好或变小的量 |
| optimization | 优化 | Searching for model settings that improve results | 找到更好的模型内部设置 |
| optimizer | 优化器 | An algorithm that updates model parameters | 按误差自动调整模型参数的算法 |
| gradient | 梯度 | A direction indicating how a value should change | 告诉模型参数往哪个方向改 |
| gradient descent | 梯度下降 | Updating parameters to reduce loss | 一步步往损失更小的方向调整 |
| learning rate | 学习率 | How large each parameter update is | 每次调整模型参数的步子有多大 |
| epoch | 训练轮次 | One full pass through the training data | 把全部训练数据看完一遍 |
| batch | 批次 | A small group of examples processed together | 一次拿来训练的一小批数据 |
| mini-batch | 小批次 | A small batch used for an update | 每次更新时使用的一小组样本 |
| iteration | 迭代步骤 | One update step during training | 模型进行一次学习更新 |
| hyperparameter | 超参数 | A training choice set outside the learned values | 训练前或训练中人为设定的控制项 |
| model architecture | 模型架构 | The structure of a model | 模型由哪些部件、怎样连接组成 |
| algorithm | 算法 | A defined method for learning or prediction | 解决学习或预测问题的一套步骤 |
| linear model | 线性模型 | A model combining features with weighted sums | 把特征按权重相加来预测的模型 |
| logistic regression | 逻辑回归 | A model often used for classification probabilities | 常用来预测类别概率的模型 |
| decision tree | 决策树 | A model that makes decisions through branching rules | 像流程图一样逐层判断的模型 |
| random forest | 随机森林 | An ensemble of many decision trees | 把很多决策树组合起来的模型 |
| gradient-boosted trees | 梯度提升树 | Trees built sequentially to correct earlier errors | 一棵棵树接力修正前面错误的模型 |
| support vector machine | 支持向量机 | A model that separates classes with a boundary | 找一条边界把不同类别分开的模型 |
| k-nearest neighbors | K近邻 | Predicting from the most similar nearby examples | 看附近最相似的几个例子来判断 |
| neural network | 神经网络 | A model made of connected learned units | 由许多相连计算单元组成的模型 |
| deep learning | 深度学习 | Machine learning using neural networks with many layers | 用很多层神经网络学习复杂规律 |
| ensemble model | 集成模型 | A model combining several models | 把多个模型的结果合在一起 |
| model family | 模型家族 | A group of related model types | 一类有共同结构或方法的模型 |
| baseline | 基线模型 | A simple reference model for comparison | 用来做对照的简单模型 |
| rule-based programming | 基于规则的编程 | Behavior specified by rules written by people | 人直接写出“如果…那么…”规则 |
| fixed-rule programming | 固定规则编程 | Programming with explicitly fixed rules | 规则预先写死，程序自己不从例子学 |
| decision boundary | 决策边界 | A boundary separating predicted classes | 模型用来区分不同类别的分界线 |
| generalization | 泛化 | Performing well on new, similar data | 不只会背训练题，还能做好新题 |
| generalize | 泛化 | Apply learned patterns beyond training examples | 把学到的规律用到没见过的新数据 |
| overfitting | 过拟合 | Fitting training data too closely and failing on new data | 训练题做得很好，但新题不会 |
| underfitting | 欠拟合 | Being too simple to capture useful patterns | 模型太简单，连训练数据都学不好 |
| memorization | 记忆化 | Remembering examples instead of learning general patterns | 只背答案，没有真正学会规律 |
| data leakage | 数据泄漏 | Information from evaluation data improperly enters training | 测试答案偷偷流进训练，导致成绩虚高 |
| distribution shift | 数据分布变化 | The real-world data differs from training data | 上线后的数据和训练时不是同一种情况 |
| concept drift | 概念漂移 | The relationship between inputs and outcomes changes | 世界规则变了，原来的规律不再适用 |
| covariate shift | 协变量偏移 | Input distribution changes while the target relation may stay similar | 输入样本的组成变了 |
| out-of-distribution data | 分布外数据 | Data unlike what the model learned from | 和训练数据差异很大的新数据 |
| data drift | 数据漂移 | Data characteristics change over time | 数据的特征随时间发生变化 |
| monitoring | 监控 | Continuously checking system behavior after release | 上线后持续查看模型表现和数据变化 |
| deployment | 部署 | Putting a trained model into real use | 把训练好的模型接入真实业务 |
| production | 生产环境 | The live environment used by real users | 真正服务用户的运行环境 |
| post-deployment | 部署后 | The period after a model is released | 模型上线之后的阶段 |
| human review | 人工复核 | A person checks or decides based on model output | 由人检查模型结果再做决定 |
| appropriate human review | 适当的人工复核 | Human oversight suited to the risk and task | 根据风险高低安排合适的人来把关 |
| reliable use | 可靠使用 | Using the model with evidence and safeguards | 有评估、有边界、有保护措施地使用模型 |
| representative labels | 有代表性的标签 | Labels that reflect real cases fairly | 标签能覆盖真实世界的重要情况 |
| evaluation | 评估 | Measuring whether the system meets expectations | 检查模型是否达到要求 |
| model evaluation | 模型评估 | Testing a model against data and goals | 用数据和目标检验模型表现 |
| metric | 指标 | A number used to measure performance | 衡量模型好坏的数字 |
| performance | 性能 / 表现 | How well the model performs its task | 模型完成任务的效果 |
| accuracy | 准确率 | The fraction of predictions that are correct | 所有预测里答对的比例 |
| precision | 精确率 | Of predicted positives, the fraction truly positive | 模型说“是”的里面有多少真的“是” |
| recall | 召回率 | Of true positives, the fraction found | 所有真的“是”里模型找出了多少 |
| F1 score | F1分数 | A balance of precision and recall | 综合精确率和召回率的分数 |
| confusion matrix | 混淆矩阵 | A table of correct and incorrect class predictions | 展示各种分类答对答错情况的表 |
| true positive | 真阳性 | Correctly predicting the positive class | 真的为正，模型也判断为正 |
| true negative | 真阴性 | Correctly predicting the negative class | 真的为负，模型也判断为负 |
| false positive | 假阳性 | Predicting positive when it is negative | 实际不是，却被模型说成是 |
| false negative | 假阴性 | Predicting negative when it is positive | 实际是，却被模型漏掉了 |
| mean squared error | 均方误差 | Average squared distance between values | 把预测差距平方后取平均 |
| mean absolute error | 平均绝对误差 | Average absolute prediction difference | 预测差距绝对值的平均数 |
| calibration | 校准 | Whether predicted probabilities match real frequencies | 模型说70%可能发生时，长期是否真的约70%发生 |
| threshold | 阈值 | A cutoff used to turn a score into a decision | 分数超过某条线才判为某类 |
| decision threshold | 决策阈值 | The cutoff for making a classification decision | 把概率或分数变成最终类别的界线 |
| ranking metric | 排名指标 | A metric for whether items are ordered well | 衡量推荐或结果排序是否合理的指标 |
| held-out evaluation | 留出评估 | Evaluating on data not used for fitting | 用模型没见过的数据检查效果 |
| validation check | 验证检查 | A check during model development | 开发过程中用验证数据做检查 |
| test set performance | 测试集表现 | Results measured on the test set | 模型在最终测试数据上的成绩 |
| error analysis | 错误分析 | Studying where and why predictions fail | 逐类查看模型错在哪里、为什么错 |
| edge case | 边界案例 | An unusual or difficult input | 少见、特殊或很难处理的情况 |
| failure mode | 失败模式 | A recurring way the system can fail | 模型反复出现的一种失败方式 |
| robustness | 鲁棒性 / 稳健性 | Staying useful under variation or disturbance | 数据有变化时仍能保持表现 |
| fairness | 公平性 | Avoiding unjustified differences across groups | 不因人群身份而产生不合理差别 |
| bias | 偏差 | A systematic tendency toward certain errors | 模型长期朝某个方向错的倾向 |
| harmful error | 有害错误 | An error that can cause meaningful harm | 会造成实际伤害的预测错误 |
| safety | 安全性 | Avoiding dangerous or unacceptable behavior | 模型不做危险或不可接受的事 |
| privacy | 隐私 | Protecting personal or sensitive information | 不让个人敏感信息被不当使用或泄露 |
| auditability | 可审计性 | Ability to inspect and review decisions or behavior | 以后能查清模型怎么运行、出了什么问题 |
| explainability | 可解释性 | Ability to give understandable reasons for outputs | 能用人听得懂的方式说明为什么这样预测 |
| accountability | 责任可追溯性 | Clear responsibility for system outcomes | 出问题时知道谁负责、如何追查 |
| feedback | 反馈 | Information used to judge or improve results | 告诉模型或团队结果好不好、哪里要改 |
| feedback loop | 反馈回路 | A repeated cycle of outputs affecting future data or training | 模型结果又影响下一轮数据和学习的循环 |
| answer key | 答案表 / 标准答案 | The correct answers used for practice | 类似练习题后面的答案册 |
| worked example | 演示例题 | An example shown together with its solution | 连问题和解法一起展示的例子 |
| teacher | 老师 | The human-like role supplying correct answers in the analogy | 类比中给出答案的人 |
| learner | 学习者 | The model-like role learning from examples in the analogy | 类比中通过练习学规律的一方 |
| question | 问题 | A case presented for an answer | 要模型回答的题目或任务 |
| practice | 练习 | Repeated exposure to examples during learning | 通过反复看例子来学习 |
| useful pattern | 有用规律 | A pattern that helps predict correctly | 真能帮助模型答对的规律 |
| task | 任务 | The real-world job the model must perform | 模型要完成的具体事情 |
| intended task | 预期任务 | The task for which the model is designed | 模型原本被设计来做的事情 |
| task success | 任务成功 | Whether the model accomplishes the intended job | 模型有没有完成目标 |
| output type | 输出类型 | The kind of result returned by a model | 模型输出是类别、数字、概率还是排序 |
| new case | 新案例 | A future example requiring a prediction | 之后遇到的一个新情况 |
| real-world example | 现实世界示例 | A practical case showing how the method is used | 展示真实业务用途的例子 |
| business example | 业务示例 | An example from an organizational task | 来自企业业务的应用案例 |
| application domain | 应用领域 | The area where a model is used | 模型服务的行业或场景 |

## Potential Missing Concepts

- **Training/validation/test split**: The page mentions held-out data, but does not explicitly define the full three-way split or cross-validation.
- **Features and feature engineering**: Inputs are described, but how useful features are selected, transformed, or encoded is not explained.
- **Loss, optimizer, gradient descent, and learning rate**: The page says internal values are adjusted to reduce errors, but omits the usual optimization mechanics.
- **Overfitting, underfitting, regularization, and bias-variance trade-off**: Generalization is implied, but common causes and controls for poor generalization are absent.
- **Data leakage**: A major reason evaluation can look falsely strong, not covered in the source page.
- **Class imbalance**: Important for spam, credit risk, and other classification tasks where one class is rare.
- **Threshold selection and calibration**: The page names probabilities and risk scores but does not explain how scores become decisions.
- **Confusion-matrix metrics**: Accuracy, precision, recall, F1, false positives, and false negatives would make the classification examples more concrete.
- **Regression metrics**: Mean absolute error, mean squared error, and related measures are not named.
- **Cross-validation**: A common way to estimate performance when data is limited.
- **Data preprocessing**: Cleaning, missing values, scaling, encoding, and normalization are not described.
- **Feature scaling**: Especially relevant to distance-based and gradient-based algorithms.
- **Categorical and numerical features**: The source uses mixed examples but does not distinguish feature types.
- **Time-series split**: Demand forecasting needs time-aware validation rather than arbitrary random splitting.
- **Leakage from future information**: Particularly important in credit and demand forecasting examples.
- **Distribution shift, data drift, and concept drift**: Monitoring is named, but the kinds of change it should detect are not detailed.
- **Retraining**: The source says to monitor after deployment but does not state when or how a model should be retrained.
- **Human-in-the-loop**: Human review is named, but escalation rules and decision ownership are not explained.
- **Fairness and subgroup evaluation**: Reliable use is mentioned, but group-level performance and harm checks are not explicit.
- **Privacy and security of labeled data**: The source does not discuss sensitive labels, access control, or training-data protection.
- **Explainability and audit trails**: Useful for credit-risk and other consequential predictions, but absent from the page.
- **Model serving and latency**: Deployment is implied by monitoring, but operational serving constraints are not covered.
- **Reproducibility and versioning**: Dataset, label, model, and evaluation versions are not discussed.
- **Active learning**: A related labeled-data workflow where humans label the most informative examples.
- **Semi-supervised learning**: A nearby learning setup that combines labeled and unlabeled data.
- **Self-supervised learning**: A related setup where targets are created from the data itself rather than manual labels.
- **Transfer learning**: Reusing a pretrained model for a supervised task.
- **Fine-tuning**: Adapting a pretrained model with task-specific labeled examples.
- **Multi-task learning**: Learning several related supervised tasks together.
- **Ordinal classification**: Classification where class order matters, such as low/medium/high.
- **Ranking and learning-to-rank**: The page mentions ranking as an output but does not explain ranking objectives.
- **Probabilistic prediction**: The page names probability but does not explain distributions or uncertainty.
- **Prediction intervals / uncertainty estimation**: Especially important for demand forecasts and risk scores.
- **Cost-sensitive learning**: Treating different kinds of errors as having different business costs.
- **Reject option / abstention**: Allowing the model to defer uncertain cases to a human.
- **Calibration curve**: A practical visualization for checking predicted probabilities.
- **Data and label provenance**: Recording where examples and target answers came from.
- **Synthetic data**: Artificial examples that may supplement scarce labeled data, with associated risks.
- **Annotation agreement**: Measuring whether multiple labelers agree on an answer.
- **Label taxonomy**: The defined set of categories and their relationships.
- **Benchmark**: A repeatable dataset and task used to compare models.
- **Baseline comparison**: Checking whether a complex model beats a simple alternative.
- **Offline vs online evaluation**: Separating pre-release data tests from live business outcomes.
- **Canary deployment and rollback**: Safer ways to release a model after training.

## Aliases / Synonyms

- Supervised learning / supervised ML / supervised machine learning / label-based learning / learning with labeled examples
- Labeled data / labelled data / annotated data / tagged data / ground-truth data
- Label / class label / target label / annotation / ground truth
- Target / target value / response variable / dependent variable / outcome / ground-truth answer
- Input / instance / sample / observation / record / feature vector
- Prediction / inference result / model output / estimated outcome / predicted outcome
- Classification / categorization / class prediction / label prediction
- Regression / numeric prediction / continuous prediction
- Training / fitting / model fitting / learning phase
- Inference / prediction / scoring / serving-time prediction / application phase
- Validation set / development set / dev set / tuning set / held-out validation data
- Test set / evaluation set / holdout set / final test data
- Generalization / out-of-sample performance / performance on unseen data
- Overfitting / overtraining / memorization of the training set
- Underfitting / insufficient model capacity / high-bias fit
- Loss / objective / error function / training criterion
- Parameter / learned parameter / model weight / coefficient
- Hyperparameter / training setting / configuration parameter
- Probability score / confidence score / likelihood score / risk score
- Evaluation / model testing / performance measurement / validation of usefulness
- Monitoring / production monitoring / post-deployment observation / model surveillance
- Human review / human oversight / manual review / human-in-the-loop
- Spam filter / spam classifier / junk-mail detector
- Demand forecasting / sales forecasting / demand prediction / forecast modeling
- Credit risk scoring / default prediction / repayment-risk prediction

## Do Not Confuse Candidates

- **Supervised Learning vs Machine Learning**: Supervised Learning is one learning setup inside the broader Machine Learning field.
- **Supervised Learning vs Artificial Intelligence**: Artificial Intelligence is the broad field; supervised learning is one way to build predictive systems.
- **Supervised Learning vs Rule-based programming**: Supervised learning learns patterns from examples; rule-based programming uses rules explicitly written by people.
- **Supervised Learning vs Unsupervised Learning**: Supervised learning uses known labels or target answers; unsupervised learning looks for structure without predefined answers.
- **Supervised Learning vs Reinforcement Learning**: Supervised learning learns from labeled examples; reinforcement learning learns through actions, feedback, and rewards.
- **Supervised Learning vs Deep Learning**: Supervised learning describes the source of learning signal; deep learning describes a model approach that may be trained with supervision.
- **Label vs Feature**: A label is the answer to predict; a feature is an input property used to make that prediction.
- **Target vs Prediction**: The target is the known or desired answer; the prediction is what the model produces.
- **Training data vs Test data**: Training data teaches the model; test data checks it after fitting.
- **Validation data vs Test data**: Validation data helps choose or tune a model; test data should provide a more independent final check.
- **Classification vs Regression**: Classification predicts categories; regression predicts numerical values.
- **Binary classification vs Multiclass classification**: Binary classification has two classes; multiclass classification has more than two possible classes.
- **Multiclass vs Multilabel classification**: Multiclass selects one class; multilabel can assign several classes to one example.
- **Probability vs Confidence**: A probability should have a defined interpretation; a confidence score may be an uncalibrated model score.
- **Accuracy vs Precision**: Accuracy counts all correct predictions; precision focuses on how trustworthy positive predictions are.
- **Precision vs Recall**: Precision asks how many predicted positives are correct; recall asks how many real positives were found.
- **False positive vs False negative**: A false positive is an incorrect positive alert; a false negative is a missed positive case.
- **Score vs Decision**: A score is often continuous; a decision applies a threshold or policy to choose an action or class.
- **Model parameter vs Hyperparameter**: Parameters are learned from data; hyperparameters are selected as training controls.
- **Training vs Inference**: Training changes or fits the model; inference uses the fitted model without learning from that case in the usual workflow.
- **Error vs Loss**: Error can mean an individual mistake or difference; loss is the formal quantity optimized during training.
- **Generalization vs Memorization**: Generalization works on new data; memorization mainly repeats training examples.
- **Overfitting vs High accuracy**: High training accuracy alone does not prove good generalization.
- **Monitoring vs Evaluation**: Evaluation is a planned measurement; monitoring is ongoing observation, especially after deployment.
- **Human review vs Guaranteed correctness**: Human review adds a safeguard; it does not make every model prediction correct.
- **Risk score vs Risk decision**: A risk score estimates risk; a person or policy may still need to decide what action to take.
- **Representative labels vs Perfect labels**: Representative labels cover real cases fairly; no label set is automatically perfect.
- **Model performance vs Business outcome**: A metric can improve without improving the real decision or business result.
- **Correlation vs Causation**: A learned predictive pattern may help forecast an outcome without causing it.
- **Prediction vs Explanation**: A model can predict well without explaining why the relationship exists.
- **Deep Learning vs Neural Network**: Deep learning usually implies many layers; a neural network can be shallow or deep.
- **Supervised Learning vs Generative AI**: Supervised learning is a learning setup; Generative AI is a goal or family of systems that create new content.
- **Labeled data vs Human understanding**: A label supplies an operational answer; it does not mean the model understands the concept like a person.

## Notes

- Source page was read in full, including the definition, answer-key analogy, five-step process, spam filtering, credit-risk, demand-forecasting examples, misconceptions, related-concepts map, takeaway, and video placeholder.
- Primary source wording emphasizes: labeled examples; input-target pairs; learned patterns; prediction errors; held-out data; generalization; class/number/probability/ranking outputs; and monitoring after deployment.
- Related context reviewed: `ai-foundations.html`, `machine-learning.html`, `unsupervised-learning.html`, `deep-learning.html`, and `evaluation.html`.
- Raw-stage policy: retain broad candidates and repeated surface forms; do not deduplicate or prune near-duplicates at this stage.
- Some candidates are directly present in the source; others are contextual glossary candidates surfaced by the page's examples and neighboring foundation topics.
- “Bias” is intentionally retained in more than one context: statistical/model bias and fairness-related social or subgroup bias are distinct senses that may need separate glossary treatment.
- “Target,” “label,” “answer,” and “ground truth” overlap in beginner explanations but are not interchangeable in every technical context.
