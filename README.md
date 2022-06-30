
## 데이터 분석 시나리오

당신은 옷을 판매하는 업체의 지난 5년 간의 상품 판매 데이터를 기반으로 여러 팀에 인사이트를 주고자 합니다.

예를 들면 아래와 같은 인사이트를 얻을 수 있습니다.

1. 이벤트를 기획하거나 새로운 상품을 기획할 때 해당 시즌에 가장 인기 있는 종류의 상품으로 기획합니다.

2. 연령층 별로 인기있는 상품을 조사하여 20-30대에게 인기 있는 상품들은 SNS을 통해 온라인 구매를 할 수 있도록 홍보하고 40-50대에게 인기 있는 상품들은 매장에 많이 비치하여 오프라인 구매를 할 수 있도록 전략을 수립합니다.



### 데이터 구조
```JSON
{
    "id": "uuid",
    "invoiceDatetime": "mm/dd/yyyy HH:MM:SS",
    "products": {
        "id": "uuid",
        "category": "string",
        "price": "float",
        "priceUnit": "dallor",
    },
    "customer": {
        "id": "uuid",
        "birthday": "mm/dd/yyyy",
        "gender": "M or F",
    }
}
```

분석을 위해 생성되는 데이터는 아래와 같은 특성을 가집니다.

1. 시간대별 구매 추이

    사용자들은 주로 일과 후에 제품을 구매하며, 새벽 및 아침에는 거의 구매하지 않습니다.

    |period       |wegiths|
    |-------------|-------|
    |00:00 ~ 08:00|1      |
    |08:00 ~ 12:00|3      |
    |12:00 ~ 18:00|6      |
    |18:00 ~ 24:00|10     |

2. 카테고리별 판매 가격 추이

    제품은 그 종류에 따라 형성되는 가격대가 상이합니다. 제품별로 전부 다르게 가집니다.

    - ~25
    - 25~50
    - 50~100
    - 100~200
    - 200~

3. 연령대별 판매 종목 추이

    사용자는 연령대에 따라 선호하는 제품이 다릅니다.

    - 20~29 (20대)
    - 30~39 (30대)
    - 40~49 (40대)
    - 50~59 (50대)


## 작업 절차

1. Data generate

    ㅁ workflow
    
    - ./file_writer.py 프로그램을 실행시켜 데이터 분석에 사용되는 데이터를 생성합니다.

    - s3 버킷을 생성합니다. `wsscc2021-data-analytics-workshop`

    - 생성된 데이터 파일을 s3 에 업로드 합니다.

2. ETL
    
    ㅁ Purpose

    - birthday(생년월일)과 invoice_datetime(주문시간)을 토대로 age(나이) 컬럼을 추가합니다.

    - JSON 포맷의 원본 데이터를 분석에 용이한 Parquet 포맷으로 변환합니다.

    - 연령대별로 데이터를 구간화(binning) 합니다.

    ㅁ workflow
    
    - AWS Glue Crawler를 통해서 Raw데이터에 대한 카탈로그 테이블을 생성합니다.

    - AWS Glue Dev Endpoint (SageMaker Notebook)을 생성합니다.

        - `sagemaker_etl.py` 파일을 참조하여 notebook을 작성하고 실행합니다.

    - AWS Glue Data Brew를 통해 Data Binning을 수행합니다.

