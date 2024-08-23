std::vector<byte> I2CScan()
{
    byte error, address;
    std::vector<byte> devices; 

    Serial.println("Scanning...");

    for (address = 1; address < 127; address++)
    {
        // The i2c_scanner uses the return value of
        // the Write.endTransmisstion to see if
        // a device did acknowledge to the address.
        Wire.beginTransmission(address);
        error = Wire.endTransmission();

        if (error == 0)
        {
            devices.push_back(address);
        }
    }
    return devices;
}