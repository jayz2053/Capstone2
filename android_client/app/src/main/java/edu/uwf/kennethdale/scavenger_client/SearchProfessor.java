package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.graphics.PorterDuff;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;


public class SearchProfessor extends AppCompatActivity implements AdapterView.OnItemSelectedListener {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.search_professor);

        // Spinner element
        Spinner dept_spinner = (Spinner) findViewById(R.id.department_spinner);
        dept_spinner.getBackground().setColorFilter(getResources().getColor(R.color.white), PorterDuff.Mode.SRC_ATOP);

        Spinner prof_spinner = findViewById(R.id.professor_spinner);
        prof_spinner.getBackground().setColorFilter(getResources().getColor(R.color.white), PorterDuff.Mode.SRC_ATOP);

        /* Spinner click listener */
        //dept_spinner.setOnItemSelectedListener(this);
        prof_spinner.setOnItemSelectedListener(this);

        //Utility dept_utility = new Utility();
        //dept_utility.populateSpinner(this, prof_spinner, "department", "name");

        Utility prof_utility = new Utility();
        prof_utility.populateSpinner(this, prof_spinner, "professor", "name");

        Button homeScreen_button = findViewById(R.id.homeScreen_button2);
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
