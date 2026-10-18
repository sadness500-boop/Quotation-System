package kr.co.stecbest.quotation;

import android.content.Context;
import android.print.PrintAttributes;
import android.print.PrintDocumentAdapter;
import android.print.PrintManager;
import android.webkit.WebView;

import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

/** 견적서 화면을 안드로이드 인쇄(프린터 · PDF로 저장)로 보냅니다. */
@CapacitorPlugin(name = "StecPrint")
public class StecPrintPlugin extends Plugin {
    @PluginMethod
    public void print(PluginCall call) {
        final String name = call.getString("name", "에스텍 견적서");
        getActivity().runOnUiThread(() -> {
            try {
                PrintManager pm = (PrintManager) getContext().getSystemService(Context.PRINT_SERVICE);
                WebView wv = getBridge().getWebView();
                PrintDocumentAdapter adapter = wv.createPrintDocumentAdapter(name);
                PrintAttributes attrs = new PrintAttributes.Builder()
                        .setMediaSize(PrintAttributes.MediaSize.ISO_A4)
                        .build();
                pm.print(name, adapter, attrs);
                call.resolve();
            } catch (Exception e) {
                call.reject("인쇄를 시작하지 못했습니다: " + e.getMessage());
            }
        });
    }
}
