import time


def safe_llm_call(func, retries=3, delay=5):
    """
    LLM安全调用（防限流 + 自动重试）
    """

    for i in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"[LLM ERROR] 第{i+1}次失败: {e}")

            # 如果是限流，等久一点
            if "RateLimit" in str(e):
                time.sleep(delay + 3)
            else:
                time.sleep(delay)

    return "LLM分析失败（多次重试）"
