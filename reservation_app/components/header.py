def branded_header(title, subtitle):
    return f"""
    <div style="
        background: linear-gradient(135deg, #6C5CE7, #a29bfe);
        padding: 2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        color: white;
        box-shadow: 0 4px 15px rgba(108,92,231,0.3);
    ">
        <h1 style="font-size:1.5rem; font-weight:700; margin:0;">{title}</h1>
        <p style="opacity:0.85; font-size:0.9rem; margin-top:0.5rem;">{subtitle}</p>
    </div>
    """