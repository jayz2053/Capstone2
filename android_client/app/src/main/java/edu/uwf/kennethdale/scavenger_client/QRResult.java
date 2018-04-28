package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class QRResult extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.qrresult);
        String[] temp;

        Intent prevScreen = getIntent();
        Bundle b = prevScreen.getExtras();
        String scanResult = b.getString("SCAN_RESULT");
        TextView test = (TextView) findViewById(R.id.textView5);

        temp = scanResult.split("/");

        test.setText("Building:  4\n" + "Room number:  " + temp[0]);


        Button searchProfessor_button = findViewById(R.id.homeScreen_button);
        searchProfessor_button.setOnClickListener(new View.OnClickListener(){
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
