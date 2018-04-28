package edu.uwf.kennethdale.scavenger_client;

import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;


public class Splash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.splash);

        new Handler().postDelayed(new Runnable() {
            public void run() {
                startActivity(new Intent(Splash.this, HomeScreen.class));
                finish();
            }
        }, 3000 );

    }
}

