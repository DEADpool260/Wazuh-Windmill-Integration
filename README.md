# Wazuh-Windmill Integration

This project documents the steps to integrate Wazuh alerts with Windmill.dev, providing a seamless solution for routing and managing Wazuh level 12 alerts.

## Summary

In my quest to identify an effective SOAR (Security Orchestration, Automation, and Response) solution for managing Wazuh level 12 alerts, I considered several options, including Shuffle, another open-source tool. Ultimately, I decided to utilize Windmill.dev for its robust capabilities. This repository documents the steps I took to successfully route Wazuh alert logs to a Windmill.dev Flow.

## Steps to Integrate

1. **Create an API Token**: Create an API token in Windmill.dev.
2. **Create a Test Flow**: Create a test flow in Windmill.dev with an input named "Input" that takes a "String" as the input parameter.
3. **Deploy the Flow**: Deploy the test flow to make it active and accessible.
4. **Copy the Flow URL**: Copy the URL from the "Details & Triggers" section of your flow.
5. **Add Integration in Wazuh**: Modify the integration configuration file in Wazuh to include a new integration for custom-windmill.
6. **Add Python Script**: Create a Python script in the `/var/ossec/integration` directory named `custom-windmill` (no `.py` extension).
7. **Create Test Alert File**: Create an `custom-alert.json` file to test the integration.
8. **Test the Integration**: Run the provided command to test if the integration works.
9. **Verify in Windmill.dev**: Check the "Run" section in Windmill.dev to confirm successful integration.

## Additional Context

I will try to make a blog for this issue, but I would like to work on this further for better integration, visibility, and reduced workload for the SOC team. If you have any feedback, suggestions, or would like to collaborate on improving this integration, please feel free to reach out. Your contributions and insights are highly valued.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
