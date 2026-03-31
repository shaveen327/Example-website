def kpi_card(label, value, icon=""):
    return f"""
    <div style="
        background:white;
        padding:1.2rem;
        border-radius:12px;
        border:1px solid #E8E8E8;
        box-shadow:0 2px 8px rgba(0,0,0,0.06);
        text-align:center;
    ">
        <div style="font-size:1.6rem; margin-bottom:0.3rem;">{icon}</div>
        <p style="
            font-size:0.8rem;
            color:#888;
            letter-spacing:0.5px;
            text-transform:uppercase;
        ">
            {label}
        </p>
        <p style="font-size:2rem; font-weight:700; margin:0;">
            {value}
        </p>
    </div>
    """