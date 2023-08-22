CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): 'https://training.team{}.training.ctf.hitb.org'.format(i)
              for i in range(1, 260 + 1)},
    'FLAG_FORMAT': r'^TEAM(?:0*(?:[1-9][0-9]?|250))_[A-Z0-9]{32}$',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

    'SYSTEM_PROTOCOL': 'hitb_http',
    'SYSTEM_URL': 'https://training.ctf.hitb.org/flags',
    'SYSTEM_TOKEN': 'CHECKSYSTEM_30_419b87324c0fa1e0f297605440ac1d9d',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 5 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': '1234',

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': '00000000000000000000'
}
