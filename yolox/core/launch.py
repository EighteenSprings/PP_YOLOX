"""
update:
    2021/12/31 single gpu support
"""
__all__ = ["launch"]

def launch(
  main_func,
  args=(),
):
  """
  Args:
    main_func:
    args(tuple):
  """
  main_func(*args)