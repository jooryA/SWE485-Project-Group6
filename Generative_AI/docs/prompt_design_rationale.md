# Prompt Engineering and Template Design

## Template 1: Zero-Shot Prompting (T1)

### 1. Template Name and ID
- **Template Name:** Zero-Shot Customer Churn Analysis
- **Template ID:** T1
- **Prompting Technique:** Zero-Shot Prompting

### 2. Intended Use Case
This template generates concise, executive-friendly customer churn risk summaries and two actionable retention recommendations using customer information and supervised machine learning predictions.

It is designed to support business decision-making without providing worked examples to the language model.

### 3. Design Rationale
Zero-Shot Prompting was selected as a baseline approach to evaluate how effectively a language model can generate structured customer retention insights using instructions alone.

The template includes a defined analyst role, a clear task, customer data placeholders, explicit instructions, constraints, and a required output format.

These elements aim to improve clarity, consistency, and relevance while reducing unsupported claims.

### 4. Prompt Structure

The template consists of:

1. **Role:** Customer retention analyst preparing reports for business executives.
2. **Task:** Analyze predicted churn risk and suggest retention actions.
3. **Input Placeholders:**
   - `{churn_prediction}`: Predicted churn class.
   - `{churn_probability}`: Estimated probability of churn.
   - `{recency_days}`: Customer recency in days.
   - `{loyalty_score}`: Customer loyalty score.
   - `{cart_abandonment_rate}`: Customer cart abandonment rate.
4. **Instructions:** Generate a risk summary and exactly two actionable retention recommendations with explanations.
5. **Constraints:** Use only the provided data, avoid invented facts or causal claims, and acknowledge uncertainty.
6. **Output Format:** Risk Summary, Retention Recommendations, and Strategic Rationale.

### 5. Example Input

The following example is synthetic and is used only to demonstrate the template structure.

- Churn Prediction: 1
- Churn Probability: 87%
- Recency Days: 45
- Loyalty Score: 25
- Cart Abandonment Rate: 70%

### 6. Illustrative Output Format

**Risk Summary:**

The model estimates an 87% churn probability for this customer, indicating elevated predicted churn risk. The available information includes 45 recency days, a loyalty score of 25, and a cart abandonment rate of 70%.

**Retention Recommendations:**

1. Consider a personalized re-engagement message to encourage the customer to return, based on the reported recency.
2. Offer checkout assistance or a cart reminder, considering the customer's cart abandonment rate.

**Strategic Rationale:**

These recommendations focus on the customer's reported recency and cart abandonment behavior. Their effectiveness is not guaranteed and would require further evaluation.

*Note: This is an illustrative example written for documentation, not an actual API-generated result.*

### 7. Assumptions and Limitations

- Churn probabilities are estimates produced by a supervised learning model, not guaranteed outcomes.
- Recommendations are based only on the provided customer features.
- The template does not establish causal relationships between customer characteristics and churn.
- The template assumes that the supplied feature values and predictions are valid.
- The language model may still produce inaccurate or unsupported recommendations.
- Actual business effectiveness cannot be confirmed without further testing.
- The template does not include customer cluster information unless explicitly added in a future version.