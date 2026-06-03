class DecisionEngine:
    def evaluate(self, d):

        if d["is_adversarial"]:

            # -------------------------------
            # HIGH RISK (STRONG SIGNALS)
            # -------------------------------
            if (
                d["confidence_drop"] > 0.15 or
                d["entropy_increase"] > 0.08 or
                d["reconstruction_error"] > 0.04
            ):
                return {
                    "status": "ALERT",
                    "risk_level": "HIGH",
                    "action": "STORE_BLOCKCHAIN"
                }

            # -------------------------------
            # MEDIUM RISK
            # -------------------------------
            elif (
                d["confidence_drop"] > 0.08 or
                d["entropy_increase"] > 0.05
            ):
                return {
                    "status": "ALERT",
                    "risk_level": "MEDIUM",
                    "action": "STORE_IPFS"
                }

            # -------------------------------
            # LOW RISK
            # -------------------------------
            else:
                return {
                    "status": "ALERT",
                    "risk_level": "LOW",
                    "action": "LOG_ONLY"
                }

        # -------------------------------
        # SAFE CASE
        # -------------------------------
        else:
            return {
                "status": "SAFE",
                "risk_level": "SAFE",
                "action": "ALLOW"
            }