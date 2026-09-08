from fastapi import APIRouter
from app.modelos.client import Client

router = APIRouter(
    prefix="/clientes",
)

CLIENT_LIST =[Client(id_=1, nome="John Doe", email="john.doe@example.com", telefone="123-456-7890"),
               Client(id_=2, nome="Jane Smith", email="jane.smith@example.com", telefone="098-765-4321")]

@router.get("/", response_model=list[Client])
async def listar_clientes():
    return CLIENT_LIST


@router.get("/{client_id}", response_model=Client | None)
async def obter_cliente(client_id: int):
    for client in CLIENT_LIST:
       if client.id_ == client_id: 
        return client