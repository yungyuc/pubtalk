void caction(double arr0[][1000], double arr1[][1000]) {
    for (int it=1; it<999; it++) {
        for (int jt=1; jt<999; jt++) {
            arr0[it][jt] += arr1[it-1][jt-1];
            arr0[it][jt] += arr1[it-1][jt  ];
            arr0[it][jt] += arr1[it-1][jt+1];
            arr0[it][jt] += arr1[it  ][jt+1];
            arr0[it][jt] += arr1[it+1][jt+1];
            arr0[it][jt] += arr1[it+1][jt  ];
            arr0[it][jt] += arr1[it+1][jt-1];
            arr0[it][jt] += arr1[it  ][jt-1];
        };
    };
};
