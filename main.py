from network_good import NetworkGood


def main():
    mock_host = "https://private-anon-c49906d99c-networkforgoodapi.apiary-mock.com"
    sandbox_host = "https://api-sandbox.networkforgood.org"

    donate_client = NetworkGood(sandbox_host)
    donate_client.auth()

    # HAITIAN EARTHQUAKE RELIEF
    ein = "271908519"

    donate_client.donate(ein)

if __name__ == '__main__':
    main()