As part of hackaton we have explored Sagemaker and its capabilities. 

### Sagemaker Canvas ###  
[Sagemaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) is a visual interface for building, training, and deploying machine learning models.
Pros:
- Easy to use
- No coding required
- Supports different algorithms
- Supports different data formats
Cons:
- Very strict data format requirements (columns cannot be named Open, Label, Index, Target, cannot start with _ or contain space etc.)
- very slow when renaming columns
- each row has to be indexed - if it is not - you need to create new dataset and new model and entire process takes a lot of time
- in the end it couldn't create model because of some error "contact aws support". Spent 2 hours on AWS support and they couldn't resolve it or find the cause of it which was a dealbreaker.
- max 13 numeric columns allowed

Overall, it is a good tool for quick prototyping and exploration of different models. However, it is not suitable for production use.

Sagemaker AutoPilot
[Sagemaker AutoPilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) is a tool for automatic model creation.
Pros:
- also easy to use and no coding required
- takes couple minutes to create first model
Cons:
- minimal number of rows 500 -> we had 460

model performance report see [report.pdf](report.pdf)
