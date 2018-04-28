package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class HomeScreen extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.home_screen);

        Button qr_button = findViewById(R.id.qr_button);
        qr_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                goToQRScanner();
            }
        });

        Button campusMap_button = findViewById(R.id.campusMap_button);
        campusMap_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                goToCampusMap();
            }
        });

        Button searchClass_button = findViewById(R.id.searchClass_button);
        searchClass_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                goToSearchClass();
            }
        });

        Button searchProfessor_button = findViewById(R.id.searchProfessor_button);
        searchProfessor_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){ goToSearchProfessor();
            }
        });
    }

    private void goToQRScanner(){
        Intent intent = new Intent(this, QRScanner.class);
        startActivity(intent);
    }

    private void goToCampusMap(){
        Intent intent = new Intent(HomeScreen.this, CampusMap.class);
        startActivity(intent);
    }

    private void goToSearchClass(){
        Intent intent = new Intent(HomeScreen.this, SearchClass.class);
        startActivity(intent);
    }

    private void goToSearchProfessor(){
        Intent intent = new Intent(HomeScreen.this, SearchProfessor.class);
        startActivity(intent);
    }

}
