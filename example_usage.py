from client import DeterministicToolCallGuardrailFirewallClient

def main():
    client = DeterministicToolCallGuardrailFirewallClient()
    res = client.inspect_tool_call_payload('execute_bash_command', '{"cmd": "rm -rf /"}', 'CONTAINER_ISOLATED')
    print('Tool Guardrail Firewall: ' + res['guardrail_evaluation_id'] + ' (Verdict: ' + res['execution_verdict'] + ')')
    print('Injection Risk: ' + str(res['injection_risk_score']) + ' | Target: ' + res['tool_target'])
    for v in res['rule_violations']:
        print('  ! ' + v)
    print('Audit Log: ' + res['security_audit_log_url'])

if __name__ == '__main__':
    main()
