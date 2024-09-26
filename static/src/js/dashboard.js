/** @odoo-module */

import { registry } from "@web/core/registry";
import { loadJS, loadCSS } from "@web/core/assets";
const { Component, onWillStart, useState, onMounted } = owl;
import { jsonrpc } from "@web/core/network/rpc_service";

export class KlinikDashboard extends Component {
  setup() {
    this.animal_state = useState({
      animal_count: 0,
      animal_ids: [],
    });

    this.client_state = useState({
      client_count: 0,
      client_ids: [],
    });

    this.dokter_state = useState({
      dokter_count: 0,
      dokter_ids: [],
    });

    this.janji_state = useState({
      janji_count: 0,
      janji_ids: [],
    });

    this.detail_state = useState({
      detail_ids: [],
    });

    this.appointment_state = useState({
      appointment_ids: [],
    });

    this.pay_state = useState({
      pay_ids: [],
    });

    this.visit_state = useState({
      visit_ids: [],
    });

    onWillStart(this.onWillStart.bind(this));
    onMounted(this.onMounted.bind(this));
  }

  async onMounted() {
    await this.loadDataTables();
  }

  async onWillStart() {
    await this.fetchDataClient();
    await this.fetchDataAnimal();
    await this.fetchDataDokter();
    await this.fetchDataJanji();
    await this.fetchDataDetail();
    await this.fetchDataJanjiHari();
    await this.fetchDataPembayaran();
    await this.fetchDataVisits();
  }

  async loadDataTables() {
    await loadJS("//code.jquery.com/jquery-3.6.0.min.js");
    await loadCSS(
      "//cdn.datatables.net/2.1.7/css/dataTables.dataTables.min.css"
    );
    await loadJS("klinik_hewan/static/src/js/table.js");
    this.initDataTables();
  }

  initDataTables() {
    $(document).ready(() => {
      $("#visitsTable").DataTable();
      $("#paymentsTable").DataTable();
      $("#appointmentsTable").DataTable();
      $("#layananTable").DataTable();
    });
  }

  async fetchDataVisits() {
    try {
      const data_result = await jsonrpc("/klinik/visit/today", {});
      this.visit_state.visit_ids = data_result;
    } catch (error) {
      console.log(error);
    }
  }

  async fetchDataPembayaran() {
    try {
      const data_result = await jsonrpc("/payments/all", {});
      this.pay_state.pay_ids = data_result.data;
    } catch (error) {
      console.log(error);
    }
  }

  async fetchDataJanjiHari() {
    try {
      const data_result = await jsonrpc("/janji/day", {});
      this.janji_state.janji_ids = data_result.appointments;
      this.janji_state.janji_count = data_result.appointments.length;
    } catch (error) {
      console.log(error);
    }
  }

  async fetchDataDetail() {
    try {
      const data_result = await jsonrpc("/layanan/data", {});
      console.log(data_result);
      this.detail_state.detail_ids = data_result.data;
    } catch (error) {
      console.log(error);
    }
  }

  async fetchDataJanji() {
    try {
      const data_result = await jsonrpc("/get/janji/data", {});
      this.janji_state.janji_count = data_result.count;
      this.janji_state.janji_ids = data_result.ids;
    } catch (error) {
      console.error("Error fetching janji data:", error);
    }
  }

  async fetchDataDokter() {
    try {
      const data_result = await jsonrpc("/get/dokter/data", {});
      this.dokter_state.dokter_count = data_result.count;
      this.dokter_state.dokter_ids = data_result.ids;
    } catch (error) {
      console.error("Error fetching dokter data:", error);
    }
  }

  async fetchDataClient() {
    try {
      const data_result = await jsonrpc("/get/client/data", {});
      this.client_state.client_count = data_result.count;
      this.client_state.client_ids = data_result.ids;
    } catch (error) {
      console.error("Error fetching client data:", error);
    }
  }

  async fetchDataAnimal() {
    try {
      const data_result = await jsonrpc("/get/animal/data", {});
      this.animal_state.animal_count = data_result.count;
      this.animal_state.animal_ids = data_result.ids;
    } catch (error) {
      console.error("Error fetching animal data:", error);
    }
  }

  _onClickAnimals() {
    const animal_ids = this.animal_state.animal_ids;
    if (animal_ids) {
      console.log(animal_ids);
    }
  }
}

// Register the component with the Odoo registry
KlinikDashboard.template = "KlinikDashBoardMain";
registry.category("actions").add("klinik_dashboard_main", KlinikDashboard);
