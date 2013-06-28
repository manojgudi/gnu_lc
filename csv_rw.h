void update_csv_knob(float);

void update_csv_knob(float value)
{
        float v1;
        int f1;


        FILE *fp, *fp2;

        printf("hello");
        fp = fopen("results.dat","rt");
        fscanf(fp,"%f, %i", &v1, &f1);
        fclose(fp);

        if (f1 == 1){
                fp2 = fopen("results.dat","w");
                int flag=0;
                fprintf(fp2,"%f, %i",value,flag);
                fclose(fp2);
        }


}

