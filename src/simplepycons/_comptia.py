#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class ComptiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "comptia"

    @property
    def original_file_name(self) -> "str":
        return "comptia.svg"

    @property
    def title(self) -> "str":
        return "CompTIA"

    @property
    def primary_color(self) -> "str":
        return "#C8202F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CompTIA</title>
     <path d="M11.8292 11.7067v1.8524a.608.608 0 0
 1-.6016-.6136v-1.2366a.5728.5728 0 0 0-1.1428 0v1.8502a.5988.5988 0 0
 1-.5998-.5978v-1.2524a.5746.5746 0 0 0-1.1455 0v1.2431a.608.608 0 0
 1-.5998.6071V11.709c.0097-.6352.5325-1.1422
 1.1676-1.1325h.0013c.331-.0046.6486.1302.8754.3713a1.1752 1.1752 0 0
 1 .868-.3713c.6372-.013 1.1642.493 1.1772
 1.1303zm7.0156-2.2917v3.563a.597.597 0 0 0
 .6006.5811v-3.563a.5969.5969 0 0 0-.6006-.5811zM24
 13.5258c-.324.0269-.675-.0697-.8011-.3435l-.3185-.6852h-2.1306l-.3157.7037c-.1494.2785-.544.3667-.8476.3667l1.738-3.8063a.5292.5292
 0 0 1 .4762-.3435.5367.5367 0 0 1 .481.3435L24
 13.5258zm-1.3759-1.6182-.8059-1.7671-.8038
 1.767h1.6097zm-19.166.6387a1.8463 1.8463 0 0 1-1.1817.4373c-.9312
 0-1.6888-.6824-1.6888-1.5133s.7604-1.5058
 1.6888-1.5058c.501.0002.98.2055 1.3257.5682a.5812.5812 0 0 0
 .7417.0827c-.362-.7502-1.1763-1.2376-2.0693-1.2376C1.0212 9.3778 0
 10.3164 0 11.4722c0 1.1558 1.0175 2.0953 2.2745 2.0953a2.3846 2.3846
 0 0 0 1.2885-.3713c.2605-.162.4823-.379.6499-.636a.5886.5886 0 0
 0-.7548-.0139zm11.43-2.539h1.2877v2.9512a.5904.5904 0 0 0
 .5728.6006h.0278v-3.5518h1.284a.5941.5941 0 0 0
 .5932-.5932h-4.3503a.5904.5904 0 0 0 .5848.5932zm-7.3108 2.0665c0
 .8364-.726 1.4853-1.6507 1.4853-.9283
 0-1.6505-.6498-1.6505-1.4853s.725-1.4947 1.6505-1.4947c.9256 0
 1.6507.6583 1.6507
 1.4947zm-.6007-.0028c0-.5004-.4641-.894-1.05-.894-.5876
 0-1.0509.3927-1.0509.894 0 .5013.4643.8875 1.051.8875s1.05-.387
 1.05-.8875zm6.7975-1.5002c-.9506 0-1.6395.6433-1.6395
 1.5178v2.5335a.596.596 0 0 0 .6016-.5857v-1.9496c0-.6313.5162-.9172
 1.038-.9172.5486 0 .9812.3982.9812.9051 0
 .4874-.4326.8754-.9813.8754-.3686
 0-.6452-.0928-.8132-.2785v.0056a.7503.7503 0 0 0-.0381.1068.596.596 0
 0 0 .4112.7241c.1462.0314.2953.0463.4447.0446.8885 0 1.581-.6508
 1.5736-1.4761a1.4647 1.4647 0 0 0-.4642-1.075 1.642 1.642 0 0
 0-1.114-.4308z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.comptia.org/newsroom/media-librar'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
