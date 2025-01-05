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


class EasyjetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "easyjet"

    @property
    def original_file_name(self) -> "str":
        return "easyjet.svg"

    @property
    def title(self) -> "str":
        return "easyJet"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>easyJet</title>
     <path d="M2.964 12.225H1.463c-.066 0-.099.029-.099.086 0
 .138.075.269.225.391.15.122.311.184.484.184.102 0
 .216-.02.34-.059.125-.039.227-.088.308-.145.072-.051.13-.077.172-.077.055
 0 .11.034.163.102a.34.34 0 0 1 .08.211c0
 .153-.096.301-.287.444-.339.253-.729.38-1.172.38-.447
 0-.822-.13-1.124-.39a1.6 1.6 0 0 1-.364-.463 1.611 1.611 0 0
 1-.189-.76c0-.358.109-.679.326-.964.187-.247.426-.431.715-.552.217-.092.452-.137.706-.137.404
 0 .748.115
 1.031.345.143.115.258.251.345.409.1.179.15.353.15.524a.617.617 0 0
 1-.086.34c-.057.087-.132.131-.223.131zm-1.418-.597h.323c.136 0
 .204-.063.204-.188a.4.4 0 0 0-.099-.281.335.335 0 0
 0-.259-.109.328.328 0 0 0-.281.141.445.445 0 0 0-.096.265c0
 .064.015.109.046.134.031.025.085.038.162.038zm3.693-1.156c.37 0
 .684.094.942.281.136.1.232.215.286.343.054.129.081.306.081.532l-.006.476c0
 .33.023.544.07.642.023.047.046.077.067.089a.41.41 0 0 0
 .134.035c.068.011.102.055.102.134a.54.54 0 0 1-.123.319 1.024 1.024 0
 0 1-.318.278.975.975 0 0 1-.501.141.659.659 0 0
 1-.53-.23c-.045-.055-.086-.083-.125-.083-.043
 0-.099.027-.169.08a1.202 1.202 0 0 1-.725.233c-.279
 0-.505-.06-.677-.179a.842.842 0 0 1-.268-.308.85.85 0 0
 1-.099-.398c0-.221.089-.417.268-.588.279-.268.696-.403 1.252-.406.123
 0 .201-.012.233-.037.032-.024.048-.081.048-.171
 0-.226-.023-.389-.07-.49-.047-.101-.123-.152-.23-.152a.27.27 0 0
 0-.171.058c-.05.038-.112.109-.187.211-.19.27-.387.406-.594.406a.356.356
 0 0 1-.255-.093.318.318 0 0
 1-.099-.243c0-.102.041-.204.123-.307.082-.102.193-.192.334-.268a2.557
 2.557 0 0 1 1.207-.305zm-.214 1.849a.317.317 0 0 0-.244.115.397.397 0
 0 0-.104.275c0 .102.024.185.073.248a.234.234 0 0 0 .195.094c.17 0
 .255-.144.255-.431
 0-.117-.012-.196-.037-.236-.024-.042-.07-.063-.138-.065zm3.33-1.846c.106
 0 .28.023.521.07a.685.685 0 0 0 .121.013.797.797 0 0 0
 .211-.057.357.357 0 0 1 .125-.029c.098 0
 .197.063.297.188.081.1.147.21.198.329a.81.81 0 0 1 .077.31.28.28 0 0
 1-.089.212.315.315 0 0 1-.224.085.375.375 0 0 1-.2-.054 2.06 2.06 0 0
 1-.283-.24c-.136-.132-.249-.198-.339-.198a.214.214 0 0
 0-.155.065.21.21 0 0 0-.065.155c0
 .104.1.202.3.294.36.162.636.339.827.53.162.162.243.36.243.594 0
 .296-.13.543-.39.741a1.307 1.307 0 0 1-.821.259c-.083
 0-.234-.014-.453-.041a7.38 7.38 0 0 0-.348-.035.505.505 0 0 0-.096.01
 1.244 1.244 0 0 1-.134.013.342.342 0 0 1-.236-.077 1.107 1.107 0 0
 1-.243-.372 1.111 1.111 0 0 1-.112-.436c0-.196.077-.294.23-.294.06 0
 .114.02.164.059.05.039.155.144.315.315.087.094.16.158.217.193a.348.348
 0 0 0 .185.053c.07 0 .127-.019.169-.056a.187.187 0 0 0
 .064-.149c0-.096-.082-.183-.246-.262-.343-.168-.59-.342-.742-.521a.928.928
 0 0
 1-.228-.62c0-.253.078-.472.233-.655.221-.261.524-.392.907-.392zm4.994
 1.571l-.422 1.159a4.405 4.405 0 0 1-.315.704 2.064 2.064 0 0
 1-.359.465c-.277.264-.61.396-1 .396-.315
 0-.571-.083-.766-.249a.613.613 0 0
 1-.227-.489c0-.164.053-.302.158-.414a.512.512 0 0 1 .388-.168c.153 0
 .277.051.37.153a.418.418 0 0 1
 .089.125c.015.036.037.116.067.24.023.094.077.141.16.141a.204.204 0 0
 0 .166-.086.336.336 0 0 0
 .067-.214c0-.1-.055-.267-.166-.501l-.77-1.638a1.506 1.506 0 0
 0-.182-.319.908.908 0 0 0-.268-.156.234.234 0 0 1-.11-.101.274.274 0
 0 1-.046-.145c0-.189.188-.318.565-.386.251-.045.538-.067.859-.067.226
 0 .403.023.533.07.175.062.262.167.262.316a.35.35 0 0
 1-.073.188.332.332 0 0 0-.07.182c0
 .051.011.104.034.16.022.055.07.149.142.281.081.149.152.224.214.224.066
 0 .134-.065.204-.196a.802.802 0 0 0 .105-.378.357.357 0 0
 0-.08-.24c-.081-.096-.121-.178-.121-.246
 0-.109.072-.195.217-.26.145-.065.338-.097.581-.097.451 0
 .677.109.677.326a.263.263 0 0 1-.069.19.658.658 0 0 1-.251.136.49.49
 0 0 0-.243.192c-.091.139-.199.374-.32.702zm3.189-2.816c.238 0
 .481.021.728.064.202.034.347.081.434.141.087.06.131.142.131.246a.23.23
 0 0 1-.048.155.715.715 0 0
 1-.208.136c-.123.064-.194.139-.212.225s-.035.421-.05
 1.004c-.006.564-.012.903-.018 1.016a2.208 2.208 0 0
 1-.04.329c-.062.311-.186.555-.374.731-.153.145-.35.259-.591.342a2.316
 2.316 0 0 1-.76.125 2.81 2.81 0 0 1-.711-.093 2.26 2.26 0 0
 1-.618-.255.975.975 0 0 1-.345-.362.985.985 0 0
 1-.128-.487c0-.213.067-.389.201-.529a.672.672 0 0 1 .505-.209c.198 0
 .366.059.505.176a.56.56 0 0 1 .208.441c0
 .045-.013.119-.038.224a.38.38 0 0 0-.006.07.21.21 0 0 0
 .073.166.285.285 0 0 0 .195.064.4.4 0 0 0
 .345-.192c.087-.128.131-.296.131-.505l-.003-.291-.006-.782a20.503
 20.503 0 0 0-.043-.838.438.438 0 0 0-.072-.206.28.28 0 0 0-.085-.083
 1.304 1.304 0 0 0-.2-.061.217.217 0 0 1-.131-.089.259.259 0 0
 1-.054-.156c0-.115.045-.207.136-.276.09-.069.238-.125.442-.168a3.3
 3.3 0 0 1 .707-.073zm4.155 2.995h-1.501c-.066 0-.099.029-.099.086 0
 .138.075.269.225.391.15.122.311.184.484.184.102 0
 .216-.02.34-.059.125-.039.227-.088.308-.145.072-.051.13-.077.172-.077.055
 0 .11.034.163.102a.34.34 0 0 1 .08.211c0
 .153-.096.301-.287.444-.339.253-.729.38-1.172.38-.447
 0-.822-.13-1.124-.39a1.616 1.616 0 0
 1-.552-1.223c0-.358.109-.679.326-.964.187-.247.426-.431.715-.552.217-.092.452-.137.706-.137.404
 0 .748.115
 1.032.345.143.115.258.251.345.409.1.179.15.353.15.524a.617.617 0 0
 1-.086.34c-.059.087-.133.131-.225.131zm-1.418-.597h.323c.136 0
 .204-.063.204-.188a.4.4 0 0 0-.099-.281.335.335 0 0
 0-.259-.109.328.328 0 0 0-.281.141.445.445 0 0 0-.096.265c0
 .064.015.109.046.134.032.025.086.038.162.038zm3.761-.316v1.079c0
 .128.031.232.094.313a.292.292 0 0 0 .241.121c.083 0
 .193-.038.329-.115a.187.187 0 0 1 .096-.029c.051 0
 .098.031.141.093a.352.352 0 0 1 .063.202c0
 .132-.072.259-.217.38-.302.258-.669.386-1.099.386-.341
 0-.614-.096-.821-.289-.207-.193-.31-.447-.31-.762v-1.475c0-.049-.006-.079-.018-.091-.012-.012-.042-.018-.091-.018h-.329c-.062
 0-.101-.01-.118-.03-.017-.02-.026-.068-.026-.142v-.141c.002-.064.027-.111.073-.141l1.463-.92a.286.286
 0 0 1 .134-.029h.259c.053 0
 .089.012.107.037.018.024.027.073.027.145v.431c0
 .064.01.105.03.125.02.019.063.029.129.029h.591c.079 0
 .13.014.153.043.023.029.035.09.035.184v.188c0
 .102-.015.173-.045.212-.03.039-.084.059-.163.059h-.578c-.06
 0-.1.011-.121.032-.019.023-.029.063-.029.123z" />
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
