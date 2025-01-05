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


class SonarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonar"

    @property
    def original_file_name(self) -> "str":
        return "sonar.svg"

    @property
    def title(self) -> "str":
        return "Sonar"

    @property
    def primary_color(self) -> "str":
        return "#FD3456"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sonar</title>
     <path d="M19.63 5.037a3.834 3.834 0 0 0-.702.044 14.875 14.875 0
 0 1 1.018 5.465c0 5.693-3.172 10.745-7.802
 12.587.234.015.469.024.707.024h.035a7.434 7.434 0 0 0
 5.748-2.764c1.773-2.194 2.861-5.15 2.861-8.391a13.582 13.582 0 0
 0-1.865-6.965Zm-.738 5.509a13.833 13.833 0 0
 0-.98-5.172c-.136.056-.233.107-.304.142a.8.8 0 0
 0-.424.804c.083.72.126 1.444.127 2.169 0 3.312-1.069 6.49-3.011
 8.946-1.837 2.321-4.301 3.815-6.981 4.242l.023.014a5.457 5.457 0 0 0
 5.103.153c3.782-1.854 6.447-6.22 6.447-11.298ZM24 12.002a11.104
 11.104 0 0 0-.85-4.276 4.892 4.892 0 0 0-1.072-1.627 3.61 3.61 0 0
 0-.842-.631A3.598 3.598 0 0 0 21 5.356a14.841 14.841 0 0 1 1.544
 6.642c0 3.294-1.073 6.467-2.982 8.901A11.135 11.135 0 0 0 24
 12.002Zm-3.147-7.771A11.118 11.118 0 0 0 12.856.843C6.691.843 1.64
 5.95 1.702 12.115c.013 1.461.315 2.905.888
 4.25-.184-.024-.369-.032-.555-.024-.5.023-1.207-.157-1.527-.247-.32-.089-.606.167-.476.465v.009c1.108
 2.536 3.562 4.187 5.906 4.182.155 0 .311-.008.466-.024 5.488-.418
 9.843-5.746 9.843-12.236 0-.409-.018-.816-.053-1.22a.238.238 0 0
 0-.054-.132.237.237 0 0 0-.263-.075.24.24 0 0 0-.117.084c-1.518
 2.009-3.766 5.541-6.579
 3.7-1.084-.706-1.661-2.225-1.335-3.772.586-2.777 3.822-4.608
 5.248-4.034.112.045.513.205.65.571.208.558-.421 1.018-.742 2.007-.345
 1.071-.15 2.206.092 2.256.271.054.726-.94 1.845-1.844.813-.654
 1.426-.839 1.811-1.534.371-.678-.29-1.392-.065-1.456.225-.063.435.717
 1.105 1.105.559.325 1.058.122 1.794.092.273-.002.545.019.813.063 0 0
 .144.02.372.067a.077.077 0 0 0 .052-.003.084.084 0 0 0
 .04-.034.076.076 0 0 0 .012-.051.082.082 0 0 0-.02-.049Zm-8.314
 8.599a.786.786 0 0 1 .508-.307.648.648 0 0 1
 .499.135c.271.251.191.736-.042
 1.015-.217.258-.644.427-.941.236a.678.678 0 0 1-.263-.542.8.8 0 0 1
 .239-.537Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
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
