/** @odoo-module */

import { registry } from '@web/core/registry';
const { Component, onWillStart, useState } = owl;
import { jsonrpc } from '@web/core/network/rpc_service';

export class KlinikDashboard extends Component {
  setup() {
    this.animal_state = useState({
      animal_count: 0,
      animal_ids: []
    });

    this.client_state = useState({
      client_count: 0,
      client_ids: []
    });

    this.dokter_state = useState({
      dokter_count: 0,
      dokter_ids: []
    });

    this.janji_state = useState({
      janji_count: 0,
      janji_ids: []
    });

    onWillStart(this.onWillStart.bind(this));
  }

  async onWillStart() {
    await this.fetchDataClient();
    await this.fetchDataAnimal();
    await this.fetchDataDokter();
    await this.fetchDataJanji();
  }

  async fetchDataJanji() {
    try {
      const data_result = await jsonrpc('/get/janji/data', {});
      console.log(data_result)
      this.janji_state.janji_count = data_result.count;
      this.janji_state.janji_ids = data_result.ids;
    } catch (error) {
      console.error('Error fetching client data:', error);
    }
  }

  async fetchDataDokter() {
    try {
      const data_result = await jsonrpc('/get/dokter/data', {});
      this.dokter_state.dokter_count = data_result.count;
      this.dokter_state.dokter_ids = data_result.ids;
    } catch (error) {
      console.error('Error fetching client data:', error);
    }
  }

  async fetchDataClient() {
    try {
      const data_result = await jsonrpc('/get/client/data', {});
      this.client_state.client_count = data_result.count;
      this.client_state.client_ids = data_result.ids;
    } catch (error) {
      console.error('Error fetching client data:', error);
    }
  }

  async fetchDataAnimal() {
    try {
      const data_result = await jsonrpc('/get/animal/data', {});
      this.animal_state.animal_count = data_result.count;
      this.animal_state.animal_ids = data_result.ids;
    } catch (error) {
      console.error('Error fetching animal data:', error);
    }
  }

  _onClickAnimals() {
    const animal_ids = this.animal_state.animal_ids;
    if (animal_ids) {
      console.log(animal_ids);
    }
  }
}

KlinikDashboard.template = 'KlinikDashBoardMain';
registry.category('actions').add('klinik_dashboard_main', KlinikDashboard);
