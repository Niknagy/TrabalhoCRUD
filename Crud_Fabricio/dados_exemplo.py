#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para popular o banco de dados com dados de exemplo.
Execute este script para carregar alguns fretes de teste.
"""

from database import init_db, criar_frete

def popular_exemplos():
    """Insere dados de exemplo no banco de dados."""
    
    print("🚚 Populando banco de dados com exemplos...")
    
    exemplos = [
        {
            "caminhao": "Volvo FH 16 450CV",
            "motorista": "João Silva",
            "origem": "São Paulo - SP",
            "destino": "Rio de Janeiro - RJ",
            "carga": "2500 kg de eletrônicos",
            "valor": 1500.00,
            "status": "Ativo",
            "data_entrega": "2026-03-28"
        },
        {
            "caminhao": "Scania R440",
            "motorista": "Maria Santos",
            "origem": "Belo Horizonte - MG",
            "destino": "Brasília - DF",
            "carga": "3000 kg de alimentos",
            "valor": 1200.00,
            "status": "Pendente",
            "data_entrega": "2026-03-26"
        },
        {
            "caminhao": "Mercedes Benz Axor",
            "motorista": "Carlos Oliveira",
            "origem": "Salvador - BA",
            "destino": "Recife - PE",
            "carga": "1800 kg de têxteis",
            "valor": 900.00,
            "status": "Entregue",
            "data_entrega": "2026-03-22"
        },
        {
            "caminhao": "DAF XF 95",
            "motorista": "Ana Costa",
            "origem": "Curitiba - PR",
            "destino": "Porto Alegre - RS",
            "carga": "2200 kg de máquinas",
            "valor": 1100.00,
            "status": "Ativo",
            "data_entrega": "2026-03-27"
        },
        {
            "caminhao": "Iveco Stralis",
            "motorista": "Roberto Lima",
            "origem": "Manaus - AM",
            "destino": "Belém - PA",
            "carga": "1500 kg de produtos diversos",
            "valor": 2500.00,
            "status": "Pendente",
            "data_entrega": "2026-03-30"
        }
    ]
    
    for idx, frete in enumerate(exemplos, 1):
        frete_id = criar_frete(
            frete["caminhao"],
            frete["motorista"],
            frete["origem"],
            frete["destino"],
            frete["carga"],
            frete["valor"],
            frete["status"],
            frete["data_entrega"]
        )
        print(f"✅ Frete {idx} cadastrado com sucesso (ID: {frete_id})")
    
    print(f"\n🎉 Total de {len(exemplos)} fretes adicionados ao sistema!")
    print("Abra http://127.0.0.1:5000 e vá até 'Consultar' para visualizá-los.")

if __name__ == "__main__":
    init_db()
    popular_exemplos()
