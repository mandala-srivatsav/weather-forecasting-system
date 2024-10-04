package com.example.wfs;

import android.Manifest;
import android.content.pm.PackageManager;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView weatherDataText, temperatureText, descriptionText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Request SMS permission at runtime
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.SEND_SMS}, 1);
        }

        // Retrieve SharedPreferences
        SharedPreferences sharedPreferences = getSharedPreferences("UserLogin", MODE_PRIVATE);

        // Check if a phone number is registered
        String registeredPhoneNumber = sharedPreferences.getString("phoneNumber", "");

        // If no phone number is registered, redirect to SignUpActivity
        if (registeredPhoneNumber.isEmpty()) {
            Intent signUpIntent = new Intent(MainActivity.this, SignUpActivity.class);
            startActivity(signUpIntent);
            finish();
            return;
        }

        // Check if the user is logged in
        boolean isLoggedIn = sharedPreferences.getBoolean("isLoggedIn", false);

        if (!isLoggedIn) {
            // If not logged in, redirect to LoginActivity
            Intent loginIntent = new Intent(MainActivity.this, LoginActivity.class);
            startActivity(loginIntent);
            finish();
            return;
        }

        // Set content view
        setContentView(R.layout.activity_main);

        // Initialize TextViews
        weatherDataText = findViewById(R.id.weatherDataText);
        temperatureText = findViewById(R.id.temperatureText);
        descriptionText = findViewById(R.id.descriptionText);

        // Fetch and display live weather data
        WeatherService weatherService = new WeatherService();
        weatherService.getWeatherData(new WeatherService.WeatherDataListener() {
            @Override
            public void onWeatherDataReceived(String data) {
                // Example parsing (Assuming data contains temperature and description)
                String temperature = "28°C";  // Replace with actual parsed data
                String description = "Clear Sky";  // Replace with actual parsed data

                weatherDataText.setText("Live Weather Data:");
                temperatureText.setText("Temp: " + temperature);
                descriptionText.setText("Description: " + description);
            }
        });
    }

    // Logout method
    private void logout() {
        SharedPreferences sharedPreferences = getSharedPreferences("UserLogin", MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean("isLoggedIn", false);
        editor.apply();

        Intent loginIntent = new Intent(MainActivity.this, LoginActivity.class);
        startActivity(loginIntent);
        finish();
    }

    // Adding logout and test SMS options to the menu
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_logout) {
            logout();
            return true;
        } else if (id == R.id.action_test_sms) {
            // Start TestSMSActivity to send test SMS
            Intent testSmsIntent = new Intent(MainActivity.this, TestSMSActivity.class);
            startActivity(testSmsIntent);
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
