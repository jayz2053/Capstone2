package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;

public class SearchClass extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.search_class);


        Button homeScreen_button = findViewById(R.id.homeScreen_button);
        homeScreen_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){ goToHomeScreen();
            }
        });
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    private void goToHomeScreen(){
        Intent intent = new Intent(this, HomeScreen.class);
        startActivity(intent);
    }
}
