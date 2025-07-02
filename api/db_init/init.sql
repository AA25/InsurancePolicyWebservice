-- SQL file to initialise appropriate database tables with dummy data

DROP TABLE IF EXISTS policies CASCADE;
DROP TABLE IF EXISTS policy_holders CASCADE;

CREATE TABLE policy_holders (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    email VARCHAR(50) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address1 VARCHAR(50) NOT NULL,
    address2 VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create a unique index on the email column for faster lookups and to enforce uniqueness
CREATE UNIQUE INDEX IF NOT EXISTS idx_policy_holders_email ON policy_holders (email);

CREATE TABLE policies (
    id SERIAL PRIMARY KEY,
    policy_holder_id INTEGER NOT NULL,
    policy_number INTEGER NOT NULL UNIQUE,
    policy_type VARCHAR(50) NOT NULL,
    policy_start_date DATE NOT NULL,
    policy_end_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    premium_amount NUMERIC(10, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,

    -- Define the foreign key constraint
    CONSTRAINT fk_policy_holder
        FOREIGN KEY (policy_holder_id)
        REFERENCES policy_holders(id)
        ON DELETE RESTRICT -- Prevents deleting a policy_holder if policies are linked to them
);

-- Create a unique index on policy_number for faster lookups and to enforce uniqueness
CREATE UNIQUE INDEX IF NOT EXISTS idx_policies_policy_number ON policies (policy_number);


-- Trigger Function and Triggers for automatic 'updated_at' column management

-- Function for policy_holders table
CREATE OR REPLACE FUNCTION update_policy_holders_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for policy_holders table
CREATE OR REPLACE TRIGGER policy_holders_updated_at_trigger
BEFORE UPDATE ON policy_holders
FOR EACH ROW
EXECUTE FUNCTION update_policy_holders_updated_at_column();


-- Function for policies table
CREATE OR REPLACE FUNCTION update_policies_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for policies table
CREATE OR REPLACE TRIGGER policies_updated_at_trigger
BEFORE UPDATE ON policies
FOR EACH ROW
EXECUTE FUNCTION update_policies_updated_at_column();

-- Insert dummy data into policy_holders table
INSERT INTO policy_holders (
    type, first_name, last_name, date_of_birth, email, phone_number,
    address1, address2, city, postal_code, country
) VALUES
(
    'Business', 'Alice', 'Smith', '1985-03-15', 'alice.smith@aviation.co.uk', '+447911123456',
    'Flat 1', '10 Downing Street', 'London', 'SW1A 2AA', 'United Kingdom'
),
(
    'Business', 'Bob', 'Johnson', '1992-11-22', 'bob.johnson@crop.co.uk', '+447922234567',
    '22B Baker Street', 'Marylebone', 'London', 'NW1 6XE', 'United Kingdom'
),
(
    'Business', 'Catherine', 'Davies', '1978-07-01', 'catherine.davies@cybertech.co.uk', '+447933345678',
    'Unit 5', 'Innovation Hub, Tech Park', 'Manchester', 'M1 7ED', 'United Kingdom'
);

-- Insert dummy data into policies table
INSERT INTO policies (
    policy_holder_id, policy_number, policy_type, policy_start_date, policy_end_date,
    status, premium_amount, currency
) VALUES
(
    (SELECT id FROM policy_holders WHERE email = 'alice.smith@aviation.co.uk'),
    100123, 'Aviation', '2024-01-01', '2025-01-01',
    'Active', 9500.00, 'GBP'
),
(
    (SELECT id FROM policy_holders WHERE email = 'bob.johnson@crop.co.uk'),
    100124, 'Crop', '2024-03-10', '2025-03-10',
    'Active', 1000.00, 'GBP'
),
(
    (SELECT id FROM policy_holders WHERE email = 'catherine.davies@cybertech.co.uk'),
    100125, 'Cyber & Tech', '2024-02-01', '2025-02-01',
    'Active', 3200.00, 'GBP'
);