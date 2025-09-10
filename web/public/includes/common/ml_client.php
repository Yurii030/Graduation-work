<?php
//web/public/includes/common/ml_client.php
//웹 연결준비

/**
 *  유아일지 텍스트를 Python 예측 스크립트로 전달하고, Json 응답을 배열로 반환
 *  현재는 CLI 방식(shell_exec)으로 간단 연결(FastAPI 전환 전 임시)
 */

 function ml_predict(string $text): array{
    $text = trim($text);
    if($text === ''){
        return ['error'=> 'empty_text'];
    }

    // Window면 'python',mac/Linux면 'python3'
    // 현재 내 컴터는 window
    $python = 'python';

    //현재 파일 위치 : web/public/includes/common
    //위에서 3단계 올라가면 web/, 거기서 ..하면 프로젝트 루트로 이동-> ml/src/predict.py
    $webRoot=dirname(__DIR__,3);
    $script = realpath($webRoot.'/../ml/src/predict.py');

    if($script ===false || !file_exists($script)){
        return['error'=>'predict_script_not_found'];
    }

    // 인젝션 방지를 위해 인자들을 반드시 escape
    $escapedScript = escapeshellarg($script);
    $escapedText =escapeshellarg($text);

    // --text 옵션으로 전달(predict.py에서 argparse로 받음)
    $cmd = "$python $escapedScript -- text $escapedText";

    // 실제 실행
    $output = shell_exec($cmd);

    if(output === null){
        return['error' => 'ml_exec_failed'];
    }

    $data = json_decode($output,true);
    if($data === null){
        //JSON 파싱 실패 시 원본 출력도 같이 반환(디버깅용)
        return ['error'=>'invalid_json','raw'=> $output];
    }
    return $data;
}


 