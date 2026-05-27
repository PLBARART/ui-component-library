def render_button(label: str, type: str = "primary", disabled: bool = False):
    """
    Reusable Button Component

    Args:
        label (str): Text displayed on the button
        type (str): Button style (primary, secondary)
        disabled (bool): Is button disabled

    Returns:
        dict: Component definition (to be used by developer)
    """

    return {
        "component": "button",
        "label": label,
        "type": type,
        "disabled": disabled
    }