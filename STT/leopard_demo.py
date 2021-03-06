#
#    Copyright 2018 Picovoice Inc.
#
#    You may not use this file except in compliance with the license. A copy of the license is located in the "LICENSE"
#    file accompanying this source.
#
#    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
#    an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
#    specific language governing permissions and limitations under the License.
#

import argparse
import os
import sys

import soundfile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../binding/python'))

from leopard import Leopard


if __name__ == '__main__':
    def abs_path(rel_path):
        return os.path.join(os.path.dirname(__file__), '../..', rel_path)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--library_path',
        help="absolute path to Leopard's dynamic library",
        default=abs_path('lib/linux/x86_64/libpv_leopard.so'))

    parser.add_argument(
        '--acoustic_model_path',
        help='absolute path to acoustic model parameter file',
        default=abs_path('lib/common/acoustic_model.pv'))

    parser.add_argument(
        '--language_model_path',
        help='absolute path to language model parameter file',
        default=abs_path('lib/common/language_model.pv'))

    parser.add_argument(
        '--license_path',
        help='absolute path to license file',
        default=abs_path('resources/license/leopard_eval_linux.lic'))

    parser.add_argument(
        '--audio_paths',
        nargs='+',
        help='absolute paths to audio files to be transcribed',
        required=True)

    args = parser.parse_args()

    leopard = Leopard(
        library_path=args.library_path,
        acoustic_model_path=args.acoustic_model_path,
        language_model_path=args.language_model_path,
        license_path=args.license_path)

    for audio_path in args.audio_paths:
        audio_path = os.path.expanduser(audio_path.strip())
        audio, sample_rate = soundfile.read(audio_path, dtype='int16')
        if sample_rate != leopard.sample_rate:
            raise ValueError('Leopard can only process audio data with sample rate of %d' % leopard.sample_rate)

        transcript = leopard.process(audio)

        print(transcript) 
