package kr.co.stecbest.quotation;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(StecPrintPlugin.class);
        super.onCreate(savedInstanceState);
    }
}
