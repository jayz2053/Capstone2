package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CampusMap extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.campus_map);

        Button homeScreen_button = findViewById(R.id.homeScreen_button);
        homeScreen_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){ goToHomeScreen();
            }
        });
    }

    private void goToHomeScreen(){
        Intent intent = new Intent(this, HomeScreen.class);
        startActivity(intent);
    }
}
