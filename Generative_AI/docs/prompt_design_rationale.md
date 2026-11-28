## Prompt Template Design Documentation

### Template 1: Zero-Shot Prompting

**Name:** Zero-Shot Prompting

**Template ID:** PT-01

**Rationale:**

The Zero-Shot prompting technique was selected as a baseline to evaluate Gemini's ability to interpret customer information and machine learning outputs without providing illustrative examples.

Zero-Shot prompting is suitable for this task because the churn prediction and customer segmentation is already performed by the machine learning model, so the required inputs, instructions, and expected output are clearly defined, making more complex reasoning techniques such as chain of thoughts or tree of thoughts were not considered necessary for the intended task. Moreover, Gemini performs well with the instruction-based prompting with clearly defined output formatting.

This approach allows us to investigate whether clear instructions alone are sufficient to generate relevant, accurate, and actionable reports before introducing examples through Few-Shot prompting.

**Intended Use Case**
This template is used to generate a customer churn risk report and provide personalized retention recommendations using customer features and machine learning outputs.
it also serves as a baseline for evaluating the Few-shot promting and deciding whether a prompt without examples can provide a better response for the AI.

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
{'churn_prediction': 1, 'churn_probability': '99.999998%', 'recency_days': 346, 'loyalty_score': 18, 'cart_abandonment_rate': '73.00%', 'kmeans_persona': 'Low-Engagement Customers', 'gmm_persona': 'One-time Buyers', 'gmm_confidence': '99.942420%'}


Example output:

            Risk Summary:
                The predictive model estimates a very high churn probability (99.999998%) for this customer, classifying them as a churn risk (Prediction: 1). Key individual features show high disengagement: 346 days of inactivity (Recency Days), a low loyalty score of 18, and a 73.00% cart abandonment rate. Contextual segmentation indicates the customer belongs to the "Low-Engagement Customers" K-Means behavioral segment and is classified as a "One-time Buyer" via GMM, with a high membership confidence of 99.94%. 

            Retention Recommendations:
                1. Re-engagement Campaign: Deploy a targeted win-back email campaign offering assistance or a tailored incentive to address the 73.00% cart abandonment rate and reactivate the customer after 346 days of inactivity.
                2. Loyalty Incentive: Introduce a streamlined onboarding or first-time buyer nurturing sequence designed to transition this one-time buyer into a repeat purchaser and improve their loyalty score from 18.

            Strategic Rationale:
                These recommendations align with the customer's high estimated churn risk, extended period of inactivity (346 days), and high cart abandonment rate (73.00%). By utilizing the "Low-Engagement" behavioral context and the high-confidence "One-time Buyer" classification, the strategies directly target the specific observed patterns of low purchase frequency and stalled transactions without assuming causality or guaranteed outcomes.






**Assumptions:**

- the provided customer features to the AI model is accurate, consistent and belong to the same customer
- The instructions, constraints, and required output format are sufficiently clear for the model to interpret the provided information without illustrative examples.
- Customer segmentation information supports decision-making and provides additional context for personalizing retention recommendations.

**Limitations:**

- Without illustrative examples as. a reference for guidance,the model may interpret instructions differently, resulting in variations in report quality, structure, and recommendation relevance.
- The quality and accuracy of the generated reports are highly influenced by the provided customer information and machine learning outputs.
- The usefulness of segmentation information may be limited due to the weak separation between customer segments.
- Explicit constraints can reduce the risk of hallucinations but do not eliminate it.
- The effectiveness of the generated retention recommendations has not been validated through real-world customer interventions.

-------------------


### Template 2: Few-Shot Prompting

**Name:** Few-Shot Prompting

**Template ID:** PT-02

**Rationale:**
The Few-Shot prompting technique was selected to investigate whether adding illustrative examples could improve the quality of the generated churn risk reports and personalized retention recommendations.

The template use the same base structure as the Zero-Shot template but includes two illustrative examples representing customers with different churn probabilities, behavioral characteristics, and GMM membership confidence levels.

These examples guide the model in interpreting machine learning outputs, handling uncertainty in customer segmentation, and generating relevant and actionable retention recommendations while maintaining a consistent output format.

**Intended Use Case**
This template is used to generate a customer churn risk report and provide personalized retention recommendations using customer features, machine learning outputs, and illustrative examples.
In addition, it is intended to support business executives in understanding specific customer situations and identifying personalized retention strategies, with examples guiding the AI in generating reports for different customer profiles.



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
{'churn_prediction': 1, 'churn_probability': '99.999998%', 'recency_days': 346, 'loyalty_score': 18, 'cart_abandonment_rate': '73.00%', 'kmeans_persona': 'Low-Engagement Customers', 'gmm_persona': 'One-time Buyers', 'gmm_confidence': '99.942420%'}


Example output:
            Risk Summary:
                The model estimates a churn probability of approximately 99.999998% with a churn prediction of 1, indicating a very high estimated churn risk. The customer features include 346 recency days, a loyalty score of 18, and a cart abandonment rate of 73.00%. The customer is categorized within the Low-Engagement Customers K-Means behavioral segment and classified as a One-time Buyer in the GMM purchase tier with a high GMM membership confidence of 99.942420%.

            Retention Recommendations:
                1. Send a targeted re-engagement campaign offering an incentive to encourage a second purchase, considering the customer's 346 recency days, low loyalty score of 18, and classification as a one-time buyer with high confidence.
                2. Provide a streamlined checkout reminder or assistance, considering the customer's 73.00% cart abandonment rate.

            Strategic Rationale:
                The recommendations align with the customer's high estimated churn risk, long absence, low loyalty score, and one-time buyer status. Given the very high GMM membership confidence, the purchase tier is used reliably alongside individual features and the low-engagement behavioral segment to address past abandonment and lack of repeat purchases. These interventions do not guarantee customer retention.



**Assumptions:**

- the provided customer features to the AI model is accurate, consistent and belong to the same customer
- The illustrative examples are related to the task and shows the expected report structure and interpretation of machine learning outputs.
- Providing examples may help the model understand how to personalize recommendations and handle uncertainty in customer segmentation.

**Limitations:**

- The model may rely excessively on the provided examples, which could cause repetition or less personalized recommendations in report generation.
- Including illustrative examples increases the input token count compared to Zero-Shot prompting.
- The quality and accuracy of the generated reports are highly influenced by the provided customer information and machine learning outputs.
- The usefulness of segmentation information may be limited due to the weak separation between customer segments.
- Explicit constraints can reduce the risk of hallucinations but do not eliminate it.
- The effectiveness of the generated retention recommendations has not been validated through real-world customer interventions.

--------------------------







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


## Lessons Learned

- Zero- shot prompting can successfully complete the task without illustrative examples when clear instructions are provided.
- illustrative examples can guide report generation and help the model provide concise, and personalized recommendation.
- comparing different prompting techniques helps identify their strengths, weaknesses, and trade-offs when selecting the most suitable technique for the intended task.
- Relying on a single evaluation metric is insufficient, multiple evaluation metrics should be used to assess different aspects of report quality and support comprehensive comparison.



## References

[1] Google, “Prompt design strategies,” Gemini API Documentation. Accessed: Nov. 25, 2026. [Online]. Available: https://aistudio.google.com/docs/prompting-strategies

[2] Z. Sprague et al., “To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning,” in Proc. Int. Conf. Learn. Representations (ICLR), 2025. [Online]. Available: https://arxiv.org/pdf/2409.12183

[3] T. B. Brown et al., “Language models are few-shot learners,” in Advances in Neural Information Processing Systems, vol. 33, pp. 1877–1901, 2020. [Online]. Available: https://arxiv.org/pdf/2005.14165

[4] J. Wei et al., “Finetuned language models are zero-shot learners,” in Proc. Int. Conf. Learn. Representations (ICLR), 2022. [Online]. Available: https://arxiv.org/pdf/2109.01652