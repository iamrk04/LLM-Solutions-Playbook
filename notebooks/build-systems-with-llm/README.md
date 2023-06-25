# Build Systems with LLM

Here, we will learn best practices for building a complex application using an LLM. We will use the running example of building an end-to-end customer service assistant system that chains multiple calls to a language model, using different instructions depending on the output of the prevoius call, and sometimes even looking things up from external sources.

We will perform the following steps to build this system:

- First, we will evaluate the input to make sure it doesn't contain any problematic content, such as hateful speech.
- Next, the system will process the input, It will identify what type of query this is. Is it a complaint or a product information request and so on?
- Once it has established that it is a product inquiry, it will retrieve the relevant information about the product and use a language model to write a helpful response.
- Finally, we will check the output to make sure it isn't problematic, such as inaccurate or inappropriate answers.
- At last, we will look at best practices for evaluating and improving our system over time.

Hands-on examples make each concept easy to understand. Built-in Jupyter notebooks allow you to seamlessly experiment with the code and prompts.