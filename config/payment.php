<?php
// Payment configuration (never store in version control)
// These values should be set in environment variables on the server

return [
    'payment_gateway' => [
        'url' => 'https://secure.paymentgateway.com/api',
        'key' => getenv('PAYMENT_GATEWAY_API_KEY'),
        'secret' => getenv('PAYMENT_GATEWAY_SECRET')
    ],
    'bank_accounts' => [
        'owner' => [
            'bank' => 'ABSA',
            'account_number' => getenv('ABSA_ACCOUNT_NUMBER'),
            'branch_code' => getenv('ABSA_BRANCH_CODE'),
            'percentage' => 60
        ],
        'ai_fund' => [
            'bank' => 'Capitec',
            'account_number' => getenv('CAPITEC_AI_ACCOUNT_NUMBER'),
            'branch_code' => getenv('CAPITEC_BRANCH_CODE'),
            'percentage' => 20
        ],
        'operations' => [
            'bank' => 'Capitec',
            'account_number' => getenv('CAPITEC_OPERATIONS_ACCOUNT_NUMBER'),
            'branch_code' => getenv('CAPITEC_BRANCH_CODE'),
            'percentage' => 20
        ]
    ]
];
?>
