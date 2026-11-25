## Prompt Template Design Documentation

### Template 1: Zero-Shot Prompting

**Name:** Zero-Shot Prompting

**Template ID:** PT-01

**Rationale:**

The Zero-Shot prompting technique was selected as a baseline to evaluate Gemini's ability to interpret customer information and machine learning outputs without providing illustrative examples.

The template relies on explicit instructions, relevant customer information, constraints, and a predefined output format to guide the model in generating churn risk reports and personalized retention recommendations.

This approach allows us to investigate whether clear instructions alone are sufficient to generate relevant, accurate, and actionable reports before introducing examples through Few-Shot prompting.

**Intended Use Case**
This template is intended to generate concise customer churn risk report and provide personalized retention recommendations using customer features and machine leearning outputs.
it also serves as a baseline for evaluating the Few-shot promting and deciding whether a prompt with out examples can provide a better response.

**Structure:**

The Zero-Shot template consists of six main components:

1. **Role:** Define the model's role as a customer retention analysts preparing clear and comprehensice customer reports
2. **Task:** Highlights the specific objective of the customer chrn analyzing process and providing personallized retention recommendations
3. **Customer Information:** Provides the model with churn predictions, churn probabilities, individual customer features, the customer's K-Means behavioral segment, GMM purchase tier, and GMM membership confidence through dynamic placeholders.
4. **Instructions:** Guides the model in summarizing churn risk, identifying relevant customer characteristics, and generating exactly two actionable retention recommendations with supporting rationale.
5. **Constraints:** Reduce the risk of fabricated customer information, unsupported assumptions, misleading causal interpretations, and unrealistic guarantees.
6. **Required Output Format:** Specifies the output structure consisting of three sections: Risk Summary, Retention Recommendations, and Strategic Rationale.

**Example:**

The following example shows how the Zero-Shot template is populated with customer information and machine learning outputs through dynamic placeholders. The populated template is then sent to Gemini for analysis and report generation.

Example input:
---------------------------
-----
------------------

Example input:
---------------------------
-----
------------------



**Assumptions:**

- The provided customer features and machine learning outputs are accurate, consistent, and belong to the same customer.
- The instructions, constraints, and required output format are sufficiently clear for the model to interpret the provided information without illustrative examples.
- Customer segmentation information provides additional context for personalizing retention recommendations.

**Limitations:**

- Without illustrative examples, the model may interpret instructions differently, resulting in variations in report quality, structure, and recommendation relevance.
- The quality of the generated reports depends on the quality and completeness of the provided customer information and machine learning outputs.
- The weak separation between customer segments may limit the usefulness of segmentation information for personalization.
- Explicit constraints reduce the risk of hallucinations but do not eliminate it.
- The effectiveness of the generated retention recommendations has not been validated through real-world customer interventions.


### Template 2: Few-Shot Prompting

**Name:** Few-Shot Prompting

**Template ID:** PT-02

**Rationale:**
The Few-Shot prompting technique was selected to investigate whether adding illustrative examples could improve the quality of AI-generated churn risk reports and personalized retention recommendations.

The template use the same base structure as the Zero-Shot template but includes two illustrative examples representing customers with different churn probabilities, behavioral characteristics, and GMM membership confidence levels.

These examples guide the model in interpreting machine learning outputs, handling uncertainty in customer segmentation, and generating relevant and actionable retention recommendations while maintaining a consistent output format.

**Intended Use Case**
This template is intended to generate concise customer churn risk report and provide personalized retention recommendations using customer features, machine leearning outputs, and illustrative examples.
it is particularly suitable for tasks that require consistent report structure, personalized recommendations, and careful interpretation of customer segmentation uncertainty.



**Structure:**

The Few-Shot template consists of seven main components:

1. **Role:** Define the model's role as a customer retention analysts preparing clear and comprehensice customer reports
2. **Task:** Highlights the specific objective of the customer chrn analyzing process and providing personallized retention recommendations
3. **Customer Information:** Provides the model with churn predictions, churn probabilities, individual customer features, the customer's K-Means behavioral segment, GMM purchase tier, and GMM membership confidence through dynamic placeholders.
4. **Instructions:** Guides the model in summarizing churn risk, identifying relevant customer characteristics, and generating exactly two actionable retention recommendations with supporting rationale.
5. **Constraints:** Reduce the risk of fabricated customer information, unsupported assumptions, misleading causal interpretations, and unrealistic guarantees.
6. **Required Output Format:** Specifies the output structure consisting of three sections: Risk Summary, Retention Recommendations, and Strategic Rationale.
7. **Examples:** provides two synthetic illustrative examples with different churn probability and GMM membership confidence level to guide the LLM and demonstrate the expected report structure.

**Example:**

The following example shows how the Zero-Shot template is populated with customer information and machine learning outputs through dynamic placeholders. The populated template is then sent to Gemini for analysis and report generation.


Example input:
---------------------------
-----
------------------

Example input:
---------------------------
-----
------------------



**Assumptions:**

- The provided customer features and machine learning outputs are accurate, consistent, and belong to the same customer.
- The illustrative examples are relevant to the task and demonstrate the expected report structure and interpretation of machine learning outputs.
- Providing examples may help the model understand how to personalize recommendations and handle uncertainty in customer segmentation.

**Limitations:**

- The two synthetic illustrative examples do not cover all possible customer characteristics, churn probabilities, and segmentation scenarios.
- The model may rely excessively on the provided examples, resulting in repetitive or less personalized recommendations.
- Including illustrative examples increases the input token count compared to Zero-Shot prompting.
- The quality of the generated reports depends on the quality and completeness of the provided customer information and machine learning outputs.
- The weak separation between customer segments may limit the usefulness of segmentation information for personalization.
- Explicit constraints reduce the risk of hallucinations but do not eliminate it.
- The effectiveness of the generated retention recommendations has not been validated through real-world customer interventions.




### Dynamic Placeholders

Both templates use the following dynamic placeholders:

- `{churn_prediction}`: Indicates whether the customer is predicted to churn (1) or not churn (0), obtained from Logistic Regression.
- `{churn_probability}`: Represents the estimated probability of customer churn, obtained from Logistic Regression.
- `{recency_days}`: A customer feature indicating the number of days since the customer's last purchase.
- `{loyalty_score}`: A customer feature indicating the customer's loyalty score.
- `{cart_abandonment_rate}`: A customer feature indicating the rate at which the customer abandons shopping carts without completing purchases.
- `{kmeans_persona}`: Represents the customer's behavioral segment identified by the K-Means clustering model.
- `{gmm_persona}`: Represents the customer's purchase tier identified by the Gaussian Mixture Model (GMM).
- `{gmm_confidence}`: Represents the estimated membership probability associated with the customer's assigned GMM purchase tier.



##The Thought process behind each template

The two prompting techniques, **Zero-shot** and **Few-shot**, were selected to investigate which technique produces better Ai-generated churn reports and retention recommendations.

**Zero-shot** template tests whether clear, explicit instructions are sufficient to generate a well-written and comprehensive report. it was also designed as a baseline to assess Gemini's ability to interpret customer information and machine learning outputs using instructions without illustrative examples 


**Few-shot** template adds examples to the same base structure, using customers with different churn probabilities and GMM membership confidence,It investigates whether providing representative examples could improve relevance, personalization, clarity and consistency of the generated reports

Both templates follow a common structure consisting of defined role, task description, instruction, constraints, customer information (context and input data), and output format. to ensure fair comparison, the inclusion of examples is the primary difference between two approaches.



##How domain knowledge influences Design

Domain knowledge in customer churn prediction and retention influenced the selection of input features, instructions, and constraints in both prompt templates.

Based on the exploratory data analysis conducted in Phase 1, **recency days** showed the strongest association with customer churn, while **cart abandonment rate** and **loyalty score** also demonstrated relevant relationships with churn. Therefore, these features were included in both templates to support personalization and retention recommendations.

Since Logistic regression identifies predictive relationships rather than direct causes, both templates include constraints to prevent the output from presenting customer feature as direct causes of churn. Churn probabilities are treated as model estimates rather than certain outcomes.

For Unsupervised learning, K-means provides behavioral customer segments, while GMM identifies customer purchase segments and estimates the probability of belonging to each segment.Therefore, customer segment are used as supporting context for personalization, while GMM membership confidence is considered to avoid overinterpreting uncertain customer assignments.

From a customer retention perspective, customers with different churn probabilities and behavioral characteristics may require different retention strategies. Accordingly, the templates require actionable and personalized recommendations

Finally, both templates require concise, clear and professional reports that translate machine learning outputs into meaningful business insights. Additional constraints were introduced to prevent fabricated customer information, unsupported assumptions, and unrealistic guarantees.




