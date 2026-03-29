import requests
import time

# Professional Solana Whale Tracker
# Created by Haithem0dev

def check_solana_transactions(wallet_address, api_key):
    url = f"https://mainnet.helius-rpc.com/?api-key={api_key}"
    payload = {
        "jsonrpc": "2.0",
        "id": "my-id",
        "method": "getSignaturesForAddress",
        "params": [wallet_address, {"limit": 5}]
    }
    
    try:
        response = requests.post(url, json=payload)
        signatures = response.json().get('result', [])
        
        if signatures:
            print(f"[*] Found {len(signatures)} new transactions for whale: {wallet_address}")
            for sig in signatures:
                print(f" -> Signature: {sig['signature']}")
        else:
            print("[!] No new activity found.")
            
    except Exception as e:
        print(f"[X] Error connecting to RPC: {e}")

if __name__ == "__main__":
    # Placeholder for wallet monitoring
    WHALE_WALLET = "ENTER_TARGET_WALLET_HERE"
    MY_API_KEY = "YOUR_HELIUS_API_KEY"
    
    print("--- Solana Whale Monitor Active ---")
    check_solana_transactions(WHALE_WALLET, MY_API_KEY)
