from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.rotas import client


app = FastAPI(
    title="Techlog Solutions API",
    description="CRM for Techlog Solutions",
    version="1.0.0"
)

app.include_router(client.router)

@app.get("/")
async def health_check():
    return {"status": "healthy"}    

@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Techlog Solutions - Painel de Status</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            body {
                background-color: #0f172a;
                color: #f8fafc;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }

            .card {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 12px;
                padding: 2.5rem;
                width: 90%;
                max-width: 480px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
                text-align: center;
            }

            .brand {
                font-size: 1.5rem;
                font-weight: 700;
                color: #38bdf8;
                letter-spacing: 0.5px;
                margin-bottom: 0.5rem;
                text-transform: uppercase;
            }

            .subtitle {
                font-size: 1.1rem;
                color: #94a3b8;
                margin-bottom: 2rem;
                font-weight: 400;
            }

            .status-container {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                background-color: #064e3b;
                border: 1px solid #059669;
                padding: 0.75rem 1.5rem;
                border-radius: 50px;
            }

            .status-dot {
                width: 12px;
                height: 12px;
                background-color: #34d399;
                border-radius: 50%;
                box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7);
                animation: pulse 1.8s infinite;
            }

            .status-text {
                color: #a7f3d0;
                font-weight: 600;
                font-size: 1rem;
            }

            @keyframes pulse {
                0% {
                    transform: scale(0.95);
                    box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7);
                }
                70% {
                    transform: scale(1);
                    box-shadow: 0 0 0 8px rgba(52, 211, 153, 0);
                }
                100% {
                    transform: scale(0.95);
                    box-shadow: 0 0 0 0 rgba(52, 211, 153, 0);
                }
            }

            .footer-info {
                margin-top: 2rem;
                font-size: 0.85rem;
                color: #64748b;
                border-top: 1px solid #334155;
                padding-top: 1rem;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1 class="brand">Techlog Solutions</h1>
            <h2 class="subtitle">Sistema de Gestão de Ordens de Serviço</h2>

            <div class="status-container">
                <span class="status-dot"></span>
                <span class="status-text">Status: Operacional</span>
            </div>

            <div class="footer-info">
                Serviço renderizado via FastAPI
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)